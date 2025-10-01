from django.urls import path
from .views import show_main, show_products, show_about, product_detail, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('products/', show_products, name='show_products'),
    path('about/', show_about, name='show_about'),
    path('product/<uuid:pk>/', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/edit/<uuid:pk>/', edit_product, name='edit_product'),
    path('product/delete/<uuid:pk>/', delete_product, name='delete_product'),
]