from django.urls import path

from . import views

app_name = 'projectForDBD'

urlpatterns = [
    path('', views.index, name='index'),

    path('products/', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    path('suppliers/', views.supplier_list, name='supplier_list'),

    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:pk>/', views.remove_from_cart, name='delete_from_cart'),
    path('cart/', views.show_cart, name='cart'),

    path('category/create/', views.category_create, name='category_create'),
    path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('supplier/create/', views.supplier_create, name='supplier_create'),
    path('supplier/edit/<int:pk>/', views.supplier_edit, name='supplier_edit'),
    path('supplier/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
]