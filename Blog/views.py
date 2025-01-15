from django.shortcuts import render
from .models import ExampleModel
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


class ExampleListView(ListView):
    model = ExampleModel
    template_name = 'example_list.html'
    context_object_name = 'examples'

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('author', 'category')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.select_related('author', 'category').prefetch_related('comments__author')
