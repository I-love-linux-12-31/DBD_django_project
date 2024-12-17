from django.contrib import admin
from . models import Category, Product, Customer, Supplier, Order
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    ...

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...
