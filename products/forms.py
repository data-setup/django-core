# products/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'is_active', 'category']
        # Optionally, specify widgets for certain fields, if needed
        # For example, to use a Textarea widget for the description:
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }

