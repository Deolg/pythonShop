from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from django.contrib.auth.decorators import login_required
from .cart import Cart
import pdb

@login_required
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:CartDetail')


@login_required
def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')

@login_required
def CartDetail(request):
    cart = Cart(request)
    items = cart.get_items(request)
    
    return render(request, 'cart/detail.html', {'cart': items })