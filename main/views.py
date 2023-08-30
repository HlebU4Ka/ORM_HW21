from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.

def product_detail(request):
    product = get_object_or_404(Product, id=id)
    return render(request, 'main/product_detail.html', {'product': product})

def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html', {'products': products})
