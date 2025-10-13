from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario #De la entidad o modelo Usuario
        fields = '__all__' #Con esto le digo que el formulario , tendra todo los campos de la tabla Usuario
        exclude = ['rol']   #Oculta el campo 'rol' en el formulario

class LoginForm(forms.Form): #En este caso no se crea desde la database o de un modelo , si no nosostros mismos personalizandolo en este caso para login
    email = forms.EmailField(label="Correo electronico") #type y name = email en el html
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")