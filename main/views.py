from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


def product_detail(request):
    product = get_object_or_404(Product, id=id)
    return render(request, 'blog/blogpost_form.html', {'product': product})


def home(request):
    products = Product.objects.all()
    return render(request, 'blog/blogpost_detail.html', {'products': products})

