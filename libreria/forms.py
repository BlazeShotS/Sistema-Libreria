from django import forms
from .models import Libro

#La clase LibroForm es como un helper que mezcla
#Validacion automatica de datos, Generacion del formulario HTML y Conexion al modelo libro para GUARDAR o EDITAR que por dentro usa OBJECTS
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__' #Con esto le digo que el formulario , tendra todo los campos de la tabla Libro