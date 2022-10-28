from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    

class Pregunta(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30, blank = False)
    respuesta = models.TextField(max_length = 200, blank = True)
    
    class nivel(models.IntegerChoices):
        Otra_vez = 1
        Dificil = 2
        Bien = 3
        Facil = 4

    apropiacion = models.IntegerField(choices = nivel.choices, default = 1)
    ultima_vez = models.DateTimeField(null = True, blank=True) #auto = true ??
    seccion = models.ForeignKey("MAIN.Seccion", on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.name

class RespuestasCerradas(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    respuesta_cerrada = models.CharField(max_length=30,blank=False, null=True)
    respuesta_verdadera = models.CharField(max_length=30,blank=False, null=True)
    pregunta = models.ForeignKey(Pregunta, on_delete = models.CASCADE, null = True)
    
    
    def __str__(self):
        return self.respuesta_cerrada

class Tarea(models.Model):
    
    name = models.CharField(max_length = 30, blank = False)
    #materia=models.ForeignKey("Main.Materia", on_delete = models.CASCADE, null = True)
    realizado = models.BooleanField(default = False)
    def __str__(self):
        return self.name

#clase pomodoro hay un dato tipo duration

class Pomodoro(models.Model):
    time = models.DurationField()