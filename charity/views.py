from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from charity.models import Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy("/")