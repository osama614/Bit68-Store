from django.test import TestCase
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings
# Create your tests here.

User = get_user_model()

def verify_token(token):
        try:
            peyload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT["ALGORITHM"])
            user = User.objects.get(id=peyload["user_id"])
        except jwt.ExpiredSignatureError as identifier:
            return {"Error": "expired token","message": str(identifier)}

        except jwt.DecodeError as identifier:
            return {"Error": "invalid token","message": str(identifier)}

        except Exception as e:
            return {"Error": f"This token is invalid for {e} "}
        else:
            return user

class UserTestCast(TestCase):

    def setUp(self): 
        user_a = User(username='osama', email='os@test.com')
        user_a_pw = 'osama_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
    
    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1) 
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        user_a = User.objects.get(username="osama")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )
    def test_login(self):
        res = self.client.post('/api/v1/auth/users/login/',{"username":"osama","password":self.user_a_pw})
        data = res.json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data.get("access"))
        self.assertTrue(data.get("refresh"))
        self.assertEqual(verify_token(data.get("refresh")), self.user_a)
        invalid_token = data.get('access')
        invalid_token += "fakee"
        self.assertNotEqual(verify_token(invalid_token), self.user_a)

    def test_registration(self):
        res = self.client.post('/api/v1/auth/users/signup/',{"username":"omar","email":"Bit68@info.com","password":"admin3000"})
        user_b = User.objects.get(username="omar")
        data = res.json()
        self.assertEqual(res.status_code,201)
        self.assertTrue(data.get("access_token"))
        self.assertTrue(data.get("refresh_token"))
        self.assertEqual(verify_token(data.get("refresh_token")), user_b)
        invalid_token = data.get('access_token')
        invalid_token += "fakee"
        self.assertNotEqual(verify_token(invalid_token), user_b)
        user_data = {
            "id": user_b.id,
            "username": user_b.username,
            "email": user_b.email
        }
        self.assertEqual(data.get("user_data"), user_data)
        