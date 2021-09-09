from django.urls import path
from django.views.generic import TemplateView
from .views import Title, Worldmap, Battle, Moviedex

urlpatterns = [
    path('', Title.as_view(), name='title'),
    path('worldmap/', Worldmap.as_view(), name='worldmap'),
    path('battle/<str:moviemon_id>', Battle.as_view(), name='battle'),
    path('moviedex/', Moviedex.as_view(), name='moviedex'),
    
]
