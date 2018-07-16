from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Page with Products
def ProductList(request, slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)


    return render (request, 'product/list.html', {
        'category' : category,
        'categories': categories,
        'products' :products
    })


# Page Product
def ProductDetail(request,pk):
    product = get_object_or_404(Product, id=pk, available=True)

    breadcrumbs_link = product.get_cat_list()
    category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
    breadcrumbs = zip(breadcrumbs_link, category_name)
    return render(request,'product/detail.html',{
        'product':product,
        'breadcrumbs': breadcrumbs
    })





