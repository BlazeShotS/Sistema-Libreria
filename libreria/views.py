from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all() #Obteniendo toda la informacion de libros
    return render(request, 'libros/index.html',{'libros':libros}) #libros de color naranja sera llamado en el html

def crear(request):
    formulario = LibroForm(request.POST or None) #Identificar los elementos que estan enviando atravez del formulario
    return render(request, 'libros/crear.html',{'formulario':formulario}) #formulario de color naranja sera colocado en el html

def editar(request):
    return render(request, 'libros/editar.html')
