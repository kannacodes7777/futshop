from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'brand', 'category', 'stock', 
            'rating', 'thumbnail', 'description', 'is_featured'
        ]