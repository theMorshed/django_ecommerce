from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    categories = Category.objects.all()
    products = None
    
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
    product_count = products.count()
    
    return render(request, 'store/store.html', {'products': products, 'p_count': product_count, 'categories': categories})