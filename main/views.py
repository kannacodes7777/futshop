from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

def show_main(request):
    products = Product.objects.filter(is_featured=True) 
    context = {
        'products': products
    }
    return render(request, "main.html", context)

def show_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "products.html", context)

def show_about(request):
    return render(request, "about.html")

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
