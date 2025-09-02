from django.db import models

from .choices import sexos


# Create your models here.

class Autor(models.Model):
    apellido_paterno = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento=models.DateField(verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=1, choices=sexos, default='F')

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)
    
    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='Autor'
        verbose_name_plural= 'Autores'
        db_table='Autor'
        ordering=['apellido_paterno','-apellido_materno'] #Forma descendente

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo') #verbose sirve para mostrar al usuario como se llama ese campo
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen' ,null=True) #imagenes/ es la carpeta que se creara a continuacion
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    autor = models.ForeignKey(Autor,null=True,blank=True,on_delete=models.CASCADE) #ese CASCADE es si se borra un autor se borra todo los cursos relacionados con ese libro

    #Para que en la pagina admin de django, se visualize con estos nombres
    def __str__(self):
        fila = "Título " + self.titulo + " - " + " Descripcion " + self.descripcion
        return fila
    
    #Para que se borre la imagen de la carpeta imagenes tambien
    def delete(self, using = None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()