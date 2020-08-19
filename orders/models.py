from products.models import Product

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    user = models.OneToOneField(User, related_name='orders', on_delete=models.CASCADE) # Deleting the cart while deleting the user 
    items = models.ManyToManyField(Product)
    address = models.CharField(max_length = 256)
    ordered_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.user)
