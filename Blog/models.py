from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class ActiveManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_active=True)

    class ExampleModel(models.Model):
        name = models.CharField(max_length=100)
        is_active = models.BooleanField(default=True)

        objects = models.Manager()  # стандартный менеджер
        active = ActiveManager()  # кастомный менеджер

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Post(models.Model):
    # поля
    objects = models.Manager()  # Менеджер по умолчанию
    published = PublishedPostManager()  # Кастомный менеджер

