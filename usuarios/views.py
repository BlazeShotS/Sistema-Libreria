from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm, LoginForm



# Create your views here.

def crearUsuario(request):
    formularioUsuario = UsuarioForm(request.POST or None)
    if formularioUsuario.is_valid():
        formularioUsuario.save()
        return redirect('libreria:inicio')
    return render(request, 'usuarios/crear.html',{'formularioUsuario':formularioUsuario})

def loginUsuario(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email'] #ese email viene de forms.py que fue declarado como email
        password = form.cleaned_data['password']

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            messages.error(request, "El usuario no existe")
            return render(request, 'usuarios/login.html', {'form': form})

        # Verificar la contraseña con el método del modelo
        if usuario.check_password(password):
            # Guardar sesión
            request.session['usuario_id'] = usuario.id #usuario.id , usuario.nombre , usuario.rol son los atributos del objeto que estoy accediendo, es como el getter pero aca en python no se usa getter se accede mediante el atributo y eso es como un getter 
            request.session['usuario_nombre'] = usuario.nombre
            request.session['usuario_rol'] = usuario.rol

            if usuario.rol == 'ADMIN':
                return redirect('libreria:ListarAutores')
            else:
                return redirect('libreria:libros')
        else:
            messages.error(request, "Contraseña incorrecta")
    
    return render(request, 'usuarios/login.html', {'form': form})



