from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('', include('libreria.urls')), #accediendo a todo lo que tiene libreria.urls
]