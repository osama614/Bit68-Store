
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username"]

class ProductSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(required=False)
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ('id',"seller")

