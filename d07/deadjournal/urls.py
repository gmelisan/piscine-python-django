from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('articles')), name='home'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('publications/', views.PublicashionsView.as_view(), name='publicashions'),
    path('article/<int:pk>', views.ArticleView.as_view(), name='article'),
    path('favourites/', views.FavouritesView.as_view(), name='favourites'),
    path('publish/', views.PublishView.as_view(), name='publish')
]
