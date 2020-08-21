from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product

User = get_user_model()

class CartItem(models.Model):
    item = models.ForeignKey(Cart , related_name='CartItem', on_delete=models.CASCADE)
    def __str__(self):
        return self.headline

class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE) # Deleting the cart while deleting the user 
    items = models.ManyToManyField(Product, through=CartItem)
    updated_at = models.DateTimeField(auto_now=True) 
    #total_price = products.aggregate(Sum('price'))
    
    def __str__(self):
        return str(self.user)
'''
Model:
    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total

View:
    # Inside cart function 
    total_price = user.cart.total_price()

Template (cart.html)
    {% if total_price> 0 %}
    <p>${{ total_price | floatformat:2 }}</p>
'''

    


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
    