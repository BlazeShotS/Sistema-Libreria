from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'), #name='inicio' , ese inicio tengo que poner en mi href del html o ruta mejor dicho
    path('nosotros', views.nosotros, name= 'nosotros'),

    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'), #el id, tiene que coincidir con el de mi metodo eliminnar el id, tal cual
    path('libros/editar/<int:id>', views.editar, name='detalle'),

    path('autor', views.autor, name='ListarAutores'),
    path('autor/crear', views.crearAutor, name='CrearAutor'),
    path('autor/editar/<int:id>', views.editarAutor, name='EditarAutor'),
    path('autor/eliminar/<int:id>', views.eliminarAutor, name='EliminarAutor')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #PARA LAS IMAGENES , SE PUEDAN MOSTRAR EN MI PAGINA