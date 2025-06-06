# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Página principal
    path('get_weather/', views.get_weather, name='get_weather'), # Endpoint da API
]