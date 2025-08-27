from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo') #verbose sirve para mostrar al usuario como se llama ese campo
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen' ,null=True) #imagenes/ es la carpeta que se creara a continuacion
    descripcion = models.TextField(null=True, verbose_name='Descripcion')

    #Para que en la pagina admin de django, se visualize con estos nombres
    def __str__(self):
        fila = "Título " + self.titulo + " - " + " Descripcion " + self.descripcion
        return fila
    
    #Para que se borre la imagen de la carpeta imagenes tambien
    def delete(self, using = None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()