from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from products.models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('price')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller__username', 'seller__email', 'seller__id']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class MyProductsList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        current_user = self.request.user
        products = Product.objects.filter(seller=current_user).all().order_by('price')
        return products

