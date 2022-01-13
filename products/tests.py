from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product
# Create your tests here.

User = get_user_model()

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


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
        user_b = User(username='ahmed', email='ah@test.com')
        user_b.set_password("ahmed12345")
        user_b.save()
        self.user_b = user_b
        product_1 = Product.objects.create(name="Iphone 13", price=20000, seller=user_a)

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2) 
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        
        user_a = User.objects.get(username="osama")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )
    def test_get_products(self):
        
        tokens = get_tokens_for_user(self.user_a)
        access = tokens.get('access')
        res = self.client.get('/api/v1/products/',HTTP_AUTHORIZATION=f'Bearer {access}')
        data = res.json()
        self.assertEqual(res.status_code,200)
        self.assertEqual(len(data),1)
        

    def test_get_products_by_filter(self):
        tokens = get_tokens_for_user(self.user_a)
        access = tokens.get('access')
        res = self.client.get('/api/v1/products/',{"seller__username":"osama"},HTTP_AUTHORIZATION=f'Bearer {access}')
        data = res.json()
        self.assertEqual(res.status_code,200)
        self.assertEqual(len(data),1)

    def test_post_products(self):
        tokens = get_tokens_for_user(self.user_a)
        access = tokens.get('access')
        res = self.client.post('/api/v1/products/',data={"name":"mobile samsung A21","price":5000}, HTTP_AUTHORIZATION=f'Bearer {access}')
        data = res.json()
        products = Product.objects.all()
        new_product = Product.objects.filter(name ="mobile samsung A21").first()
        self.assertEqual(res.status_code,201)
        self.assertEqual(products.count(),2)
        self.assertEqual(new_product.seller.id,self.user_a.id)

        
    def test_get_my_products(self):
        tokens = get_tokens_for_user(self.user_b)
        access = tokens.get('access')
        self.client.post('/api/v1/products/',data={"name":"mobile samsung A21","price":5000}, HTTP_AUTHORIZATION=f'Bearer {access}')
        tokens = get_tokens_for_user(self.user_a)
        access = tokens.get('access')
        res = self.client.get('/api/v1/products/me/', HTTP_AUTHORIZATION=f'Bearer {access}')
        data = res.json()
        products_count = Product.objects.all().count()
        self.assertEqual(res.status_code,200)
        self.assertEqual(len(data), 1)
        self.assertEqual(products_count, 2)
        