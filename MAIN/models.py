from distutils.command.upload import upload
from random import choices
from django.db import models
from ESTUDIO.models import Pregunta
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
import os
# Create your models here.
#Creamos la clase Register para realizar el registro del usuario
class Materia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30, blank = False)
    hora = models.TimeField(blank = False)
    profesor = models.CharField(max_length = 30, blank = False)
    profesor_email = models.EmailField(blank = False)
    OPTIONS = (
        ("Lunes", "Lunes"),
        ("Martes", "Martes"),
        ("Miércoles", "Miércoles"),
        ("Jueves", "Jueves"),
        ("Viernes", "Viernes"),
        ("Sábado", "Sábado"),
        ("Domingo", "Domingo"),
    )
    horario = MultiSelectField(choices=OPTIONS, max_length=100, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    aula = models.CharField(max_length=100, blank=True)

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
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    documento = models.FileField(null=True, blank=True, upload_to="images/") 
    materia=models.ForeignKey(Materia, blank = True, on_delete=models.CASCADE, null=True)
    #Seccion=models.ForeignKey(Seccion, blank = True, on_delete=models.CASCADE, null=True )
    docPregunta=models.ForeignKey(Pregunta, blank = True, on_delete=models.CASCADE, null=True)

    def filename(self):
        return os.path.basename(self.documento.name)


    #prioridad se puede hacer con un models.Field.choices

#Hacer modelo docs, preguntar en donde se alojan

class Tarea(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30, blank = False)
    materia=models.ForeignKey(Materia, on_delete = models.CASCADE, null = True)
    nivel_prioridad=(('Bajo', 'Bajo'),('Medio','Medio'),('Alto','Alto'))
    prioridad=models.CharField(max_length=20,choices = nivel_prioridad, default = 'Bajo')
    fecha=models.DateField(blank=False, null=True)

    def __str__(self):
        return self.name


class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    key = models.FileField(null=True, blank=True, upload_to="token files/")


    