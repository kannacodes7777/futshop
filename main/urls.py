from django.urls import path
from .views import show_main, show_about, product_page, product_detail, register_page, login_page, get_products, create_product_from_modal, update_product, delete_product_ajax, ajax_register, ajax_login, ajax_logout, show_xml, show_json, get_featured_products, ajax_edit_product, ajax_create_product, add_product_page, edit_product_page, show_my_json, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('about/', show_about, name='show_about'),
    path('products/', product_page, name='product_page'),
    path('add-product/', add_product_page, name='add_product_page'),
    path('product/<uuid:pk>/', product_detail, name='product_detail'),
    path('product/edit/<uuid:pk>/', edit_product_page, name='edit_product_page'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('my-json/', show_my_json, name='show_my_json'),
    path('ajax/get_products/', get_products, name='get_products'),
    path('ajax/create_product_from_modal/', create_product_from_modal, name='create_product_from_modal'),
    path('ajax/update_product/', update_product, name='update_product'),
    path('ajax/delete_product/', delete_product_ajax, name='delete_product'),
    path('ajax/product/edit/<uuid:pk>/', ajax_edit_product, name='ajax_edit_product'),
    path('ajax/create_product/', ajax_create_product, name='ajax_create_product'),
    path('json/', show_json, name='show_json'),
    path('ajax/register/', ajax_register, name='ajax_register'),
    path('ajax/login/', ajax_login, name='ajax_login'),
    path('ajax/logout/', ajax_logout, name='ajax_logout'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('xml/', show_xml, name='show_xml'),
    path('ajax/get_featured_products/', get_featured_products, name='get_featured_products'),
]