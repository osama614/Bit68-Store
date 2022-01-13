from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Product
# Register your models here.
User = get_user_model()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "seller")
    list_filter = ("name", "price", "seller__username")
    search_fields =("name", "seller")
