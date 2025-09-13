from django import forms
from .models import Product

class ProductForm(forms.ModelForm): # Import ModelForm untuk membuat form berdasarkan model secara automatis otomatis oleh Django
    class Meta:
        model = Product
        fields = "__all__"