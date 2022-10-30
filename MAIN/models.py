from django.db import models
from ESTUDIO.models import Pregunta
from django.contrib.auth.models import User
# Create your models here.
#Creamos la clase Register para realizar el registro del usuario
class Materia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30, blank = False)
    hora = models.TimeField(blank = False)
    profesor = models.CharField(max_length = 30, blank = False)
    profesor_email = models.EmailField(blank = False)
    def __str__(self):
        return self.name
    #UNAL vs NO UNAL

class Seccion(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30, blank = False)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Documento(models.Model):
    documento=models.FileField() #Establecer un lugar donde cargar los documentos
    Materia=models.ForeignKey(Materia, blank = True, on_delete=models.CASCADE, null=True)
    Seccion=models.ForeignKey(Seccion, blank = True, on_delete=models.CASCADE, null=True )
    docPregunta=models.ForeignKey(Pregunta, blank = True, on_delete=models.CASCADE, null=True)

    #prioridad se puede hacer con un models.Field.choices

#Hacer modelo docs, preguntar en donde se alojan

class Tarea(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30, blank = False)
    materia=models.ForeignKey(Materia, on_delete = models.CASCADE, null = True)
    nivel_prioridad=(('Bajo', 'Bajo'),('Media','Medio'),('Alto','Alto'))
    prioridad=models.CharField(max_length=20,choices = nivel_prioridad, default = 'Bajo')
    fecha=models.DateField(blank=False, null=True)
    realizado = models.BooleanField(default = False)

    def __str__(self):
        return self.name


    