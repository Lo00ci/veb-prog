from .models import ExampleModel
from .models import Post, Comment
from django.shortcuts import render
from .services import get_active_examples
from django.db import transaction

def get_active_examples():
    return ExampleModel.active.all()

def active_examples_view(request):
    examples = get_active_examples()
    return render(request, 'active_examples.html', {'examples': examples})

# Получить опубликованные посты
def get_published_posts():
    return Post.objects.filter(is_published=True).order_by('-created_at')

# Получить последние 5 комментариев к посту
def get_recent_comments(post_id):
    return Comment.objects.filter(post_id=post_id).order_by('-created_at')[:5]

# Получить посты по категории
def get_posts_by_category(category_name):
    return Post.objects.filter(category__name=category_name, is_published=True)

def create_post_with_comments(post_data, comments_data):
    from .models import Post, Comment
    with transaction.atomic():
        post = Post.objects.create(**post_data)
        for comment in comments_data:
            Comment.objects.create(post=post, **comment)
    return post

def get_optimized_posts():
    return Post.objects.select_related('author', 'category').prefetch_related('comments__author')