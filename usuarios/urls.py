from django.urls import path
from . import views

urlpatterns = [
    path('usuario/crear', views.crearUsuario, name='crearUsuario'), #name='inicio' , ese inicio tengo que poner en mi href del html o ruta mejor dicho

]