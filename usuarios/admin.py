from django.contrib import admin
from .models import Usuario

# Register your models here.
admin.site.register(Usuario) #Cuando corramos , el administrador  de django tenga la manipulacion a ese Usuario
