from .models import ExampleModel


def get_active_examples():
    return ExampleModel.active.all()


from django.shortcuts import render
from .services import get_active_examples


def active_examples_view(request):
    examples = get_active_examples()
    return render(request, 'active_examples.html', {'examples': examples})
