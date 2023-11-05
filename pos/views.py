from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product
from .forms import AddProductForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {'Products': Product.objects.all()})


def view(request, id):
    product = Product.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST or None)
        if form.is_valid():
            new_name = form.cleaned_data['product_name']
            new_description = form.cleaned_data['product_description']
            new_quantity = form.cleaned_data['product_quantity']
            new_price = form.cleaned_data['product_price']
            new_sales = form.cleaned_data['product_sales']

            new_product = Product(
                product_name = new_name,
                product_description = new_description,
                product_quantity = new_quantity,
                product_price = new_price,
                product_sales = new_sales,
            )

            new_product.save()
            return render(request, 'add_product.html', {'form': AddProductForm(), 'success': True})
    else:
        form = AddProductForm()
    return render(request, 'add_product.html', {'form': AddProductForm})


def edit_product(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'edit_record.html', {'form': form, 'success': True})
    else:
        product = Product.objects.get(pk=id)
        form = AddProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('home')


def pos(request):
    if request.method == 'POST':
        search_name = request.POST.get('name')
        add_quantity = request.POST.get('quantity')
        product_search = Product.objects.filter(product_name=search_name)
        return render(request, 'pos.html', {'datas': product_search, 'quantity': add_quantity})
    else:
        products = Product.objects.all()
        return render(request, 'pos.html', {'Products': products})