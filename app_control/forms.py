from django import forms
from .models import Inventory 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        labels = {
            'product_number': 'Product Number',
            'product_name' : 'Product Name',
            'product_quantity': 'Product Quantity',
            'product_price' : 'Product Price'
        }
        widgets = {
            'product_number': forms.NumberInput(attrs= {'class': 'form-control'}),
            'product_name' : forms.TextInput(attrs= {'class': 'form-control'}),
            'product_quantity': forms.NumberInput(attrs= {'class': 'form-control'}),
            'product_price' : forms.NumberInput(attrs= {'class': 'form-control'})
        }