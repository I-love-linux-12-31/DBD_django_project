import django_filters
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Category, Supplier, Product
# from .filters import ProductFilter, CategoryFilter, SupplierFilter

# Фильтр для товаров
class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')
    supplier = django_filters.ModelChoiceFilter(queryset=Supplier.objects.all(), label='Поставщик')

    class Meta:
        model = Product
        fields = ['title', 'price_min', 'price_max', 'supplier']

# Фильтр для категорий
class CategoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название', field_name='title')
    description =  django_filters.CharFilter(lookup_expr='icontains', label='Описание', field_name='description')

    class Meta:
        model = Category
        fields = ['title', 'description']

# Фильтр для поставщиков
class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Название')

    class Meta:
        model = Supplier
        fields = ['name']
