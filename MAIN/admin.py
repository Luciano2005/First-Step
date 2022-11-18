from re import S
from django.contrib import admin
from .models import Materia, Seccion, Documento, Tarea

# Register your models here.

admin.site.register(Materia)
admin.site.register(Seccion)
admin.site.register(Documento)
admin.site.register(Tarea)

