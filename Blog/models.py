from django.db import models


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
