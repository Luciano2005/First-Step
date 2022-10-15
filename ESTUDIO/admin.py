from django.contrib import admin
from .models import Pregunta, Tarea, Pomodoro

# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Tarea)
admin.site.register(Pomodoro)