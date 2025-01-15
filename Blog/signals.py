from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ExampleModel


@receiver(post_save, sender=ExampleModel)
def example_model_created(sender, instance, created, **kwargs):
    if created:
        print(f'Создан объект: {instance.name}')
