from django.contrib import admin
from .models import Libro #De models.py estoy importando el modelo Libro

# Register your models here.
admin.site.register(Libro) #Cuando corramos , el administrador tenga la manipulacion a ese libro 