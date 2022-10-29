from django.contrib import admin
from .models import Pregunta, Pomodoro, RespuestasCerradas

# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Pomodoro)
admin.site.register(RespuestasCerradas)
