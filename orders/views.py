from .models import Order
from .forms import OrderForm
from accounts.models import Profile
from carts.models import Cart
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 


def checkout(request, pk):
    user = request.user

    if user.is_authenticated:
        cart = user.cart   
        profile = Profile.objects.filter(user_id=user.id).first()

        if request.method == 'POST':
            form = orderForm(request.POST)

            if form.is_valid():
                form.save_order(user)
                return render(request, 'orders/order-successful.html')
        
        else:
            if not cart.items.exits():
                return redirect('cart')

            form = OrderForm(
                initial=
                {
                    'address': profile.address
                }
            )

            return render(request, 'orders/orders.html', { 'form' : form, 'cart' : cart }) # orders/ <== folder
    
    
    else:
        return redirect ('login')
    
def order_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.all()
        return render( request, 'orders/order-list.html', {'orders':orders}) # {'key':value} key will be used in the template
    else:
        return redirect('product_list')
