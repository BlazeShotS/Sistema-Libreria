from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), #name='inicio' , ese inicio tengo que poner en mi href o ruta mejor dicho
    path('nosotros', views.nosotros, name= 'nosotros'),
    path('libros', views.libros, name='libros')
]