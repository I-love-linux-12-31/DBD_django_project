from django import forms
from .models import Category, Supplier, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'image']
        widgets = {
            'contact_info': forms.Textarea(attrs={'rows': 3}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'quantity', 'supplier', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'supplier': forms.CheckboxSelectMultiple(),
        }
