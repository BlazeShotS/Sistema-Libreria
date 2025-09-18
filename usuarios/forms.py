from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__' #Con esto le digo que el formulario , tendra todo los campos de la tabla Usuario
