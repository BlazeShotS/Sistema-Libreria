from django.db import models

from .choices import sexos


# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key=True) #No es necesario crear el id , lo crea por defecto django
    apellido_paterno = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento=models.DateField(verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=1, choices=sexos, default='F')

    #Metodo personalizado
    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)
    
    #Metodo especial en python que define como se representara un objeto como cadena __str__ DJANGO lo usa automaticamente en <select>, interfaz del admin, cuando imprimo el objeto autor y cuando lo pongo en una plantilla
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name='Autor'
        verbose_name_plural= 'Autores'
        db_table='autor' #Nombre personalizado con el que se creara en la database
        ordering=['apellido_paterno','-apellido_materno'] #Forma descendente , en el admin django

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo') #verbose sirve para mostrar al usuario como se llama ese campo
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen' ,null=True) #imagenes/ es la carpeta que se creara a continuacion
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    autor = models.ForeignKey(Autor,null=True,blank=True,on_delete=models.CASCADE) #ese CASCADE es si se borra un autor se borra todo los cursos relacionados con ese libro
    #El FK se crea con el nombre del campo + el id en este caso autor + _id

    #Para que en la pagina admin de django, se visualize con estos nombres
    def __str__(self):
        fila = "Título " + self.titulo + " - " + " Descripcion " + self.descripcion
        return fila
    
    #Para que se borre la imagen de la carpeta imagenes tambien
    def delete(self, using = None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    class Meta:
        db_table = 'libro'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la categoría', unique=True)
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')

    #Metodo personalizado
    def nombre_completo(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'categoria'
        ordering = ['nombre']
