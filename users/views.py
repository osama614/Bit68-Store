from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterationSerializer, RefreshTokenSerializer
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()
# Create your views here.
class Registeration(GenericAPIView):
    
    serializer_class = RegisterationSerializer
    def post(self, request):

        serializer = RegisterationSerializer(data=request.data)


        if serializer.is_valid():
            
            try:
                serializer.save()
                data = {"user_data": serializer.data}
                username = serializer.data.get('username')
                email = serializer.data.get('email')
                user = User.objects.filter(username=username).first()
                token = RefreshToken.for_user(user)
                access_token = str(token.access_token)
                data["access_token"] = str(access_token)
                data["refresh_token"] = str(token)

            except Exception as e:
                return Response({"message": f"error {e}"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(GenericAPIView):
    """This API Take a valid refresh token from the current user then he destroy it so
        you can't use it any more and you then delete the 'access_token' from your local storege and redirect the user to the login page.

    """
    serializer_class = RefreshTokenSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Your are logged out!"},status=status.HTTP_204_NO_CONTENT)