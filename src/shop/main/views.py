from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Page with Products
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    return render (request, 'product/list.html', {
        'category' : category,
        'categories': categories,
        'products' :products
    })


# Page Product
def ProductDetail(request,pk):
    product = get_object_or_404(Product, id=pk, available=True)
    return render(request,'product/detail.html',{
        'product':product
    })





