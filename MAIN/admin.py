from re import S
from django.contrib import admin
from .models import Materia, Seccion, Register, Documento

# Register your models here.

admin.site.register(Materia)
admin.site.register(Seccion)
admin.site.register(Register)
admin.site.register(Documento)
