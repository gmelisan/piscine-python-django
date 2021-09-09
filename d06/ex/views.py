import random

from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Tip
from .forms import TipForm


class IndexView(CreateView):
    template_name = 'ex/index.html'
    model = Tip
    fields = ['content']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tips'] = Tip.objects.all().order_by('-date')
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# Old version. Works but worse
class IndexView2(TemplateView):
    template_name = 'ex/index.html'

    def get(self, request):
        tips = Tip.objects.all().order_by('-date')
        form = TipForm()
        context = {
            'tips': tips,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = TipForm(request.POST)
        if form.is_valid():
            Tip.objects.create(content=form.cleaned_data['content'],
                               author=self.request.user)
        return redirect('index')
    

    
class RegistrationView(FormView):
    template_name = 'ex/registration.html'
    form_class = UserCreationForm # it's a ModelForm
    success_url = reverse_lazy('index')

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(request)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    
class LoginView(FormView):
    template_name = 'ex/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(request)

    def form_valid(self, form):
        u = form.cleaned_data['username']
        p = form.cleaned_data['password']

        user = authenticate(username=u, password=p)
        if not user:
            return super().form_invalid(form)
        login(self.request, user)
        return super().form_valid(form)

    
class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        response = redirect('index')
        response.delete_cookie('name')
        return response


class TipView(TemplateView):

    def get(self, request, tip_id):
        
        action = request.GET.get('action')
        if not action:
            return redirect('index')
        if not self.request.user.is_authenticated:
            messages.error(request, 'Login to vote')
            return redirect('index')
        if action == 'delete':
            Tip.objects.get(id=tip_id).delete()
        if action == 'upvote':
            tip = Tip.objects.get(id=tip_id)
            tip.vote(request.user, True)
        if action == 'downvote':
            tip = Tip.objects.get(id=tip_id)
            tip.vote(request.user, False)
        
        return redirect('index')
    
