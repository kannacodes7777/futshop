from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
from .models import Product
from .forms import ProductForm
import json

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(is_featured=True)
    context = {
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'N/A')
    }
    return render(request, "main.html", context)

def show_about(request):
    return render(request, "about.html", {'last_login': request.COOKIES.get('last_login', 'N/A')})

@login_required(login_url='/login')
def product_page(request):
    return render(request, "products.html")

@login_required(login_url='/login')
def add_product_page(request):
    form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required(login_url='/login')
def edit_product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

@login_required(login_url='/login')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'last_login': request.COOKIES.get('last_login', 'N/A')
    }
    return render(request, 'product_detail.html', context)

def register_page(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def get_products(request):
    product_fields = [
        'id', 'name', 'price', 'description', 'thumbnail', 'category',
        'is_featured', 'stock', 'rating', 'brand'
    ]
    products = list(Product.objects.filter(user=request.user).values(*product_fields))
    if not products:
        return JsonResponse({'status': 'empty'})
    return JsonResponse({'status': 'success', 'products': products})

@login_required
def get_featured_products(request):
    product_fields = ['id', 'name', 'price', 'category', 'thumbnail']
    products = list(Product.objects.filter(is_featured=True).values(*product_fields))
    if not products:
        return JsonResponse({'status': 'empty'})
    return JsonResponse({'status': 'success', 'products': products})

@login_required
def ajax_create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return JsonResponse({'status': 'success', 'message': 'Product added successfully!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@login_required
def create_product_from_modal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Product.objects.create(
            user=request.user,
            name=data.get('name'),
            price=data.get('price'),
            brand=data.get('brand'),
            category=data.get('category'),
            stock=data.get('stock'),
            rating=data.get('rating'),
            thumbnail=data.get('thumbnail'),
            description=data.get('description'),
            is_featured=data.get('is_featured', False)
        )
        return JsonResponse({'status': 'success', 'message': 'Product created successfully!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@login_required
def update_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            product = Product.objects.get(pk=data.get('id'), user=request.user)
            product.name = data.get('name')
            product.price = data.get('price')
            product.brand = data.get('brand')
            product.category = data.get('category')
            product.stock = data.get('stock')
            product.rating = data.get('rating')
            product.thumbnail = data.get('thumbnail')
            product.description = data.get('description')
            product.is_featured = data.get('is_featured', False)
            product.save()
            return JsonResponse({'status': 'success', 'message': 'Product updated successfully!'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product not found or you do not have permission.'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@login_required
def delete_product_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            product = Product.objects.get(pk=data.get('id'), user=request.user)
            product.delete()
            return JsonResponse({'status': 'success', 'message': 'Product deleted.'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product not found or you do not have permission.'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@login_required
def ajax_edit_product(request, pk):
    try:
        product = Product.objects.get(pk=pk, user=request.user)
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found or you do not have permission.'}, status=404)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Product updated successfully!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)
    

def ajax_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = UserCreationForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Registration successful!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

def ajax_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = AuthenticationForm(request, data=data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            response_data = {'status': 'success', 'message': 'Login successful!'}
            response = JsonResponse(response_data)
            
            current_time = timezone.now().strftime("%d %b %Y, %H:%M")
            response.set_cookie('last_login', current_time)
            return response
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

def ajax_logout(request):
    logout(request)
    response = JsonResponse({'status': 'success', 'message': 'You have been logged out.'})
    response.delete_cookie('last_login') 
    return response

def show_xml(request):
    data = serializers.serialize('xml', Product.objects.all())
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    data = serializers.serialize('json', Product.objects.all())
    return HttpResponse(data, content_type="application/json")


def show_xml_by_id(request, id):
    product = Product.objects.filter(pk=id)
    data = serializers.serialize('xml', product)
    return HttpResponse(data, content_type="application/xml")

def show_json_by_id(request, id):
    product = Product.objects.filter(pk=id)
    data = serializers.serialize('json', product)
    return HttpResponse(data, content_type="application/json")