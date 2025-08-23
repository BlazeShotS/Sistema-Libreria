from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo') #verbose sirve para mostrar al usuario como se llama ese campo
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen' ,null=True) #imagenes/ es la carpeta que se creara a continuacion
    descripcion = models.TextField(null=True, verbose_name='Descripcion')