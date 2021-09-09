from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *

class IndexView(CreateView):
    template_name = 'index.html'
    model = Picture
    fields = ['title', 'image']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pictures'] = Picture.objects.all().order_by('-date')
        return context

    def form_valid(self, form):
        print('form valid')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid')
        return super().form_invalid(form)
