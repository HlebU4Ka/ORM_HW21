from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        product_post = self.get_object()
        product_post.views += 1
        product_post.save()
        return super().get(request, *args, **kwargs)

# def product_detail(request):
#     product = get_object_or_404(Product, id=id)
#     return render(request, 'main/product_detail.html', {'product': product})
#
#
# def home(request):
#     products = Product.objects.all()
#     return render(request, 'main/home.html', {'products': products})
