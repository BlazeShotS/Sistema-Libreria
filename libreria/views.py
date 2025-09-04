from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro , Autor
from .forms import LibroForm , AutorForm


# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def libros(request):
    libros = Libro.objects.all() #Obteniendo toda la informacion de libros , el objects es como el repository en java spring boot
    return render(request, 'libros/index.html',{'libros':libros}) #libros de color naranja sera llamado en el html

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None) #SE CONSTRUYE VACIO,  los campos del formulario , segun el modelo
    if formulario.is_valid(): #Valida que el formulario no este vacio
        formulario.save() #GUARDO EN LA BD
        return redirect('libros') #Redirige a la vista libros que es el que esta en el urls.py libros de la linea 12
    return render(request, 'libros/crear.html',{'formulario':formulario}) #formulario de color naranja sera colocado en el html

def editar(request, id):
    libro = Libro.objects.get(id=id) #Busca el libro con ese id
    formulario = LibroForm(request.POST or None, request.FILES or None , instance=libro) # SE CONSTRUYE LLENO , el formulario , los inputs se inicializan ya llenados con los datos de libro que fue colocado en instance
    if formulario.is_valid() and request.POST: #Si el formulario es valido, que no este vacio  y hay un envio POST
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html',{'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')


#Para Autor
def autor(request):
    autores = Autor.objects.all()
    return render(request, 'autor/listar.html',{'autores':autores})

def crearAutor(request):
    formularioAutor = AutorForm(request.POST or None)
    if formularioAutor.is_valid():
        formularioAutor.save()
        return redirect('ListarAutor')
    return render(request, 'autor/crear.html',{'formularioAutor':formularioAutor})

