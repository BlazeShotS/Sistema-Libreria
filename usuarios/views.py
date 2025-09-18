from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm



# Create your views here.

def crearUsuario(request):
    formularioUsuario = UsuarioForm(request.POST or None)
    if formularioUsuario.is_valid():
        formularioUsuario.save()
        return redirect('libreria:inicio')
    return render(request, 'usuarios/crear.html',{'formularioUsuario':formularioUsuario})
