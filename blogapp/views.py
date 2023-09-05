from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'blogposts'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    context_object_name = 'blogpost'

    def get(self, request, *args, **kwargs):
        blogpost = self.get_object()
        blogpost.views_count += 1  # Увеличиваем счетчик просмотров на 1
        blogpost.save()
        return super().get(request, *args, **kwargs)


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'content', 'is_published']

    def form_valid(self, form):
        blogpost = form.save()
        return redirect('blog_post_detail', slug=blogpost.slug)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'content', 'is_published']

    def form_valid(self, form):
        blogpost = form.save()
        return redirect('blog_post_detail', slug=blogpost.slug)
