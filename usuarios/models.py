from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Usuario(models.Model):
    ROLES = ( #Tupla
        ('ADMIN','Administrador'),
        ('CLIENT','Cliente')
    )

    nombre = models.CharField(max_length=50, verbose_name='Nombre Completo')
    apellido = models.CharField(max_length=50, verbose_name='Apellido completo')
    edad = models.PositiveIntegerField(verbose_name='Ingrese su edad')
    email = models.EmailField(unique=True, verbose_name='Ingrese su email')
    password = models.CharField(max_length=128, verbose_name='Ingrese su password')
    rol = models.CharField(max_length=10, choices=ROLES, default='CLIENT')

    def save(self, *args, **kwargs):
        # Si la contraseña no está en hash, la encripta antes de guardar
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Verifica si la contraseña ingresada coincide con el hash"""
        return check_password(raw_password, self.password)

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido} ({self.rol})"    

    #Metodo especial en python que define como se representara un objeto como cadena __str__ DJANGO lo usa automaticamente en <select>, interfaz del admin, cuando imprimo el objeto autor y cuando lo pongo en una plantilla
    def __str__(self):
        return self.nombre_completo() #LLamo a la funcion   

    class Meta:        
        verbose_name='Usuario'
        verbose_name_plural= 'Usuarios'
        db_table='usuario' #Nombre personalizado con el que se creara en la database
        ordering=['nombre','apellido'] #Forma descendente , en el admin django
    
    