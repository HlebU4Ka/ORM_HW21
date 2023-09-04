from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
)

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog_post_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('post/<slug:slug>/edit/', BlogPostUpdateView.as_view(), name='blog_post_update'),
]
