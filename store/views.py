from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category

def store(request,category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category = categories,is_available=True)
        count = products.count()
    
    else:
        products = Product.objects.filter(is_available=True)
        count = products.count()
    context = {
        'products':products,
        'count':count
    }
    return render(request,'store/store.html',context)

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug= category_slug, slug = product_slug)
    except Exception as e:
        raise e
    
    # categories = get_object_or_404(Category,slug=category_slug)
    # products = Product.objects.filter(category = categories, slug = product_slug, is_available=True)
    context = {
        'product':single_product
    }
    return render(request,'store/product-detail.html',context)
