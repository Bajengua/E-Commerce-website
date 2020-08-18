from django.urls import path
from .views import add_to_cart, cart, remove_from_cart

urlpatterns = [
    path('', cart, name='cart'),
    path('products/<product_id>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<product_id>', remove_from_cart, name='remove_from_cart'),
    #path('remove_from_cart_all', remove_from_cart_all, name='remove_from_cart_all'),
  
]
