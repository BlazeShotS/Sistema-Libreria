from django import forms
from .models import Libro, Autor,Categoria

#La clase LibroForm es como un helper que mezcla
#Validacion automatica de datos, Generacion del formulario HTML y Conexion al modelo libro para GUARDAR o EDITAR que por dentro usa OBJECTS
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__' #Con esto le digo que el formulario , tendra todo los campos de la tabla Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'