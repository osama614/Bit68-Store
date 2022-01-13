from django.urls import path
from .views import  ProductList, MyProductsList


app_name = "products"
urlpatterns = [
    
    path('', ProductList.as_view(), name='products-list'),
    path('me/', MyProductsList.as_view(), name='my-products-list'),
    
]