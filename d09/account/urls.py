from django.urls import path
from . import views

urlpatterns = [
    path('account', views.IndexView.as_view(), name='index'),
    path('logout', views.logout_view, name='logout'),
]
