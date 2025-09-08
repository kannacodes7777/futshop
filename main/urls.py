from django.urls import path
from .views import show_main, show_products, show_about, product_detail

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('products/', show_products, name='show_products'),
    path('about/', show_about, name='show_about'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]