from django.shortcuts import redirect, render
from .models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

# Show ke main pages untuk tambahan object
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get('filter')
    if filter_type == 'my':
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.filter(is_featured=True)
    
    context = {
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'N/A')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def show_products(request):
    products = Product.objects.filter(user=request.user) 
    context = {
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'N/A')
    }
    return render(request, "products.html", context)

def show_about(request):
    context = {
        'last_login': request.COOKIES.get('last_login', 'N/A')
    }
    return render(request, "about.html", context)

@login_required(login_url='/login')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'last_login': request.COOKIES.get('last_login', 'N/A')
    }
    return render(request, 'product_detail.html', context)

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form = form.save(commit = False)
        form.user = request.user
        form.save()
        return redirect('main:show_products')
    
    context = {
                'form': form,
               'last_login': request.COOKIES.get('last_login', 'N/A')
            }
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {
        'form':form,
        'last_login': request.COOKIES.get('last_login', 'N/A')
        }
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))

        current_time = timezone.now().strftime("%d %b %Y, %H:%M")
        response.set_cookie('last_login', current_time)

        return response
   else:
      form = AuthenticationForm() 
   
   context = {
       'form': form,
       'last_login': request.COOKIES.get('last_login', 'N/A')
    }
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response