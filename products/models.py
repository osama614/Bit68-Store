from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Product(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=120)
    price = models.DecimalField(verbose_name=_("price"),max_digits=10, decimal_places=5)
    seller = models.ForeignKey(User, related_name=_("seller"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


    def __str__(self):
       return f" {self.seller.username}'s Product" 