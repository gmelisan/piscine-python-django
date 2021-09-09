from django.views.generic import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

from .models import *

class ArticleListView(ListView):
    template_name = 'articles.html'
    model = Article
    ordering = ['-created']

    
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request)

    def form_valid(self, form):
        u = form.cleaned_data['username']
        p = form.cleaned_data['password']

        user = authenticate(username=u, password=p)
        if not user:
            return super().form_invalid(form)
        login(self.request, user)
        return super().form_valid(form)

class LogoutView(RedirectView):
    url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, args, kwargs)
    

class PublicashionsView(ListView):
    template_name = 'publicashions.html'
    model = Article

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        return qs

    
class ArticleView(DetailView):
    template_name = 'article.html'
    model = Article

    def post(self, request, pk): # add to favourites
        a = Article.objects.get(id=pk)
        qs = UserFavouriteArticle.objects.filter(user=self.request.user, article=a)
        if qs:
            messages.error(request, 'already added')
            return super().get(request)
        UserFavouriteArticle.objects.create(user=self.request.user, article=a)
        return super().get(request)
        

    
class FavouritesView(ListView):
    template_name = 'favourites.html'
    model = UserFavouriteArticle

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(user=self.request.user)
        return qs


class PublishView(CreateView):
    template_name = 'publish.html'
    model = Article
    fields = ['title', 'synopsis', 'content']
    success_url = reverse_lazy('publicashions')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
