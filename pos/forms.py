from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'product_quantity', 'product_price', 'product_sales']

        labels = {
            'product_name': 'Name',
            'product_description': 'Description',
            'product_quantity': 'Quantity',
            'product_price': 'Price',
            'product_sales': 'Sales'
        }

        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control'}),
            'product_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control'}),
            'product_sales': forms.NumberInput(attrs={'class': 'form-control'})
        }



