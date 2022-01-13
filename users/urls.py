from django.urls import path
from .views import  LogoutView, Registeration
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

app_name = "users"
urlpatterns = [
    path('users/signup/', Registeration.as_view()),
    path('users/login/', TokenObtainPairView.as_view(), name='login'),
    #path('users/login/', LoginView.as_view(), name='login'),
    path('users/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('users/logout/', LogoutView.as_view(), name='logout'),
]