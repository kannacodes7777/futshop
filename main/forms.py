from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'brand', 'category', 'stock', 
            'rating', 'thumbnail', 'description', 'is_featured'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'your-tailwind-classes'}),
            'price': forms.NumberInput(attrs={'class': 'your-tailwind-classes'}),
            'brand': forms.Select(attrs={'class': 'your-tailwind-classes'}),
            'category': forms.Select(attrs={'class': 'your-tailwind-classes'}),
            'stock': forms.NumberInput(attrs={'class': 'your-tailwind-classes'}),
            'rating': forms.NumberInput(attrs={'class': 'your-tailwind-classes', 'step': '0.1'}),
            'thumbnail': forms.URLInput(attrs={'class': 'your-tailwind-classes'}),
            'description': forms.Textarea(attrs={'class': 'your-tailwind-classes', 'rows': 4}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'your-tailwind-classes'}),
        }