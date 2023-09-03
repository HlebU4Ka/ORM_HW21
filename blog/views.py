from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.shortcuts import redirect
from .models import Product
from django.urls import reverse_lazy
from .models import BlogPost

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product.views += 1
        product.save()
        return super().get(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'main/product_form.html'
    fields = ['name', 'description', 'preview', 'category', 'price', 'is_published']

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    context_object_name = 'blogpost'

    def get(self, request, *args, **kwargs):
        blogpost = self.get_object()
        blogpost.views += 1  # Увеличиваем счетчик просмотров на 1
        blogpost.save()
        return super().get(request, *args, **kwargs)

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'content', 'is_published']

    def form_valid(self, form):
        blogpost = form.save()
        return redirect(reverse('blogpost_detail', args=[blogpost.slug]))