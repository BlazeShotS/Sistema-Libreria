from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('usuario/crear', views.crearUsuario, name='crearUsuario'), #name='inicio' , ese inicio tengo que poner en mi href del html o ruta mejor dicho
    path('usuario/login', views.loginUsuario, name='login'),
]