from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator

from .forms import CategoryForm, SupplierForm, ProductForm
from .models import Category, Supplier, Product
from .filters import ProductFilter, CategoryFilter, SupplierFilter

# Create your views here.
def is_admin(request) -> bool:
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin').exists():
            return True
        if request.user.is_superuser:
            return True
    return False


# Представление для создания категории
def category_create(request):
    if not is_admin(request):
        return HttpResponseForbidden("У вас нет прав для создания категории.")

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'main_form.html', {'form': form})

# Представление для редактирования категории
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if not is_admin(request):
        form = CategoryForm(instance=category)
        form.fields['title'].widget.attrs['readonly'] = True
        form.fields['description'].widget.attrs['readonly'] = True
        return render(request, 'main_form.html', {'form': form})

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'main_form.html', {'form': form})

# Представление для удаления категории
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if not is_admin(request):
        return HttpResponseForbidden("У вас нет прав для удаления категории.")

    category.delete()
    return redirect('category_list')

# Представление для создания поставщика
def supplier_create(request):
    if not is_admin(request):
        return HttpResponseForbidden("У вас нет прав для создания поставщика.")

    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()

    return render(request, 'main_form.html', {'form': form})

# Представление для редактирования поставщика
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if not is_admin(request):
        form = SupplierForm(instance=supplier)
        form.fields['name'].widget.attrs['readonly'] = True
        form.fields['contact_info'].widget.attrs['readonly'] = True
        form.fields['image'].widget.attrs['disabled'] = True
        return render(request, 'main_form.html', {'form': form})

    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)

    return render(request, 'main_form.html', {'form': form})

# Представление для удаления поставщика
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if not is_admin(request):
        return HttpResponseForbidden("У вас нет прав для удаления поставщика.")

    supplier.delete()
    return redirect('supplier_list')

# Представление для создания товара
def product_create(request):
    if not is_admin(request):
        return HttpResponseForbidden("У вас нет прав для создания товара.")

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'main_form.html', {'form': form})

# Представление для редактирования товара
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not is_admin(request):
        form = ProductForm(instance=product)
        form.fields['title'].widget.attrs['readonly'] = True
        form.fields['description'].widget.attrs['readonly'] = True
        form.fields['price'].widget.attrs['readonly'] = True
        form.fields['quantity'].widget.attrs['readonly'] = True
        form.fields['supplier'].widget.attrs['disabled'] = True
        form.fields['image'].widget.attrs['disabled'] = True
        return render(request, 'main_form.html', {'form': form})

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('projectForDBD:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'main_form.html', {'form': form})

# Представление для удаления товара
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not is_admin(request):
        return HttpResponseForbidden("У вас нет прав для удаления товара.")

    product.delete()
    return redirect('product_list')


def get_url_for_pagination(request):
    url = str(request.get_full_path())
    if '?' in url:
        endpoint, args = url.split('?')
    else:
        endpoint, args = url, ''
    args = args.split('&')
    return F"{endpoint}?{'&'.join([i for i in args if 'page' not in i.split('=')[0]])}"


def product_list(request):
    product_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    paginator = Paginator(product_filter.qs, 7)  # Показываем по 10 товаров на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'product_list.html',
        {
            'page_obj': page_obj,
            'filter': product_filter,
            "own_url": get_url_for_pagination(request),
            "user": request.user if request.user.is_authenticated else None,
            "admin": is_admin(request)
        }
    )

def category_list(request):
    category_filter = CategoryFilter(request.GET, queryset=Category.objects.all())
    paginator = Paginator(category_filter.qs, 7)  # Показываем по 7 категорий на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'category_list.html',
        {
            'page_obj': page_obj,
            'filter': category_filter,
            "own_url": get_url_for_pagination(request),
            "user": request.user if request.user.is_authenticated else None,
            "admin": is_admin(request)
        }
    )

def supplier_list(request):
    supplier_filter = SupplierFilter(request.GET, queryset=Supplier.objects.all())
    paginator = Paginator(supplier_filter.qs, 7)  # Показываем по 7 поставщиков на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'supplier_list.html',
        {
            'page_obj': page_obj,
            'filter': supplier_filter,
            "own_url": get_url_for_pagination(request),
            "user": request.user if request.user.is_authenticated else None,
            "admin": is_admin(request)
        }
    )



def index(request):
    print("INDEX")
    print(is_admin(request))
    print(request.user)
    return render(
        request,
        'index.html',
        {
            "user": request.user if request.user.is_authenticated else None,
            "admin": is_admin(request)
        }
    )

