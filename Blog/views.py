from django.shortcuts import render
from django.views.generic import ListView
from .models import ExampleModel


class ExampleListView(ListView):
    model = ExampleModel
    template_name = 'example_list.html'
    context_object_name = 'examples'
