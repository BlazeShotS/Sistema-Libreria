from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'libreria' #Define un namespace , cosa que si uso estas rutas en otras app , ya sabre de que app viene

urlpatterns = [

    path('', views.inicio, name='inicio'), #name='inicio' , ese inicio tengo que poner en mi href del html o ruta mejor dicho
    path('nosotros', views.nosotros, name= 'nosotros'),

    path('panelAdmin', views.panel, name= 'panel'),


    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'), #el id, tiene que coincidir con el de mi metodo eliminnar el id, tal cual
    path('libros/editar/<int:id>', views.editar, name='detalle'),

    path('autor', views.autor, name='ListarAutores'),
    path('autor/crear', views.crearAutor, name='CrearAutor'),
    path('autor/editar/<int:id>', views.editarAutor, name='EditarAutor'),
    path('autor/eliminar/<int:id>', views.eliminarAutor, name='EliminarAutor'),

    path('categoria', views.categoria, name='ListarCategoria'),
    path('categoria/crear', views.crearCategoria, name='CrearCategoria'),
    path('categoria/editar<int:id>', views.editarCategoria, name='EditarCategoria'),
    path('categoria/eliminar/<int:id>', views.eliminarCategoria, name='EliminarCategoria'),

    #Para el tema de catalogo
    path("Libroscategorias", views.categoriasPreview, name="categorias_preview"),
    path("Catalogocategoria/<int:categoria_id>", views.categoriaDetalle, name="categorias_detalle"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #PARA LAS IMAGENES , SE PUEDAN MOSTRAR EN MI PAGINA