from django.contrib import admin
from .models import Libro #De models.py estoy importando el modelo Libro
from .models import Autor
from .models import Categoria

# Register your models here.
admin.site.register(Libro) #Cuando corramos , el administrador tenga la manipulacion a ese libro
admin.site.register(Autor)
admin.site.register(Categoria)