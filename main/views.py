from django.shortcuts import redirect, render
from .models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .forms import ProductForm

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

def add_product(request):
    # This part handles the submitted form data
    if request.method == "POST":
        form = ProductForm(request.POST) 
        
        # Here is the validation check!
        if form.is_valid():
            form.save() # Saves to the database only if data is valid
            return redirect('main:show_products')
    
    # This part shows a blank form for a new request
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'add_product.html', context)

def show_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, id):
    product = Product.objects.filter(pk=id)
    data = serializers.serialize('xml', product)
    return HttpResponse(data, content_type="application/xml")

def show_json_by_id(request, id):
    product = Product.objects.filter(pk=id)
    data = serializers.serialize('json', product)
    return HttpResponse(data, content_type="application/json")