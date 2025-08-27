from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all() #Obteniendo toda la informacion de libros , el objects es como el repository en java spring boot
    return render(request, 'libros/index.html',{'libros':libros}) #libros de color naranja sera llamado en el html

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None) #Esto es como que le dice si hay datos en POST usalos no dejes vacio
    if formulario.is_valid():
        formulario.save() #GUARDO EN LA BD
        return redirect('libros') #Redirige a la vista libros que es el metodo libros de la linea 12
    return render(request, 'libros/crear.html',{'formulario':formulario}) #formulario de color naranja sera colocado en el html

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None , instance=libro)
    return render(request, 'libros/editar.html',{'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
