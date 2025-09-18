from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm



# Create your views here.

def crearAutor(request):
    formularioUsuario = UsuarioForm(request.POST or None)
    if formularioUsuario.is_valid():
        formularioUsuario.save()
        return redirect('')
    return render(request, '',{'':formularioAutor})
