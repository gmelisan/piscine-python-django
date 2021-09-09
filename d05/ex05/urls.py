from django.urls import path, include

from . import views

urlpatterns = [
    path('populate/', views.populate, name='populate'),
    path('display/', views.display, name='display'),
    path('remove/', views.remove, name='remove'),
]
