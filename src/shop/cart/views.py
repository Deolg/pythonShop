from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from .cart import Cart
import pdb


def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:CartDetail')



def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')


def CartDetail(request):
    cart = Cart(request)
    items = cart.get_items(request)
    pdb.set_trace()
    
    return render(request, 'cart/detail.html', {'cart': items })