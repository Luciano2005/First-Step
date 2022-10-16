from django.db import models
from ESTUDIO.models import Pregunta
# Create your models here.
#Creamos la clase Register para realizar el registro del usuario
class Register(models.Model):
    #revision id
    username=models.CharField(max_length= 30, blank= False)
    name=models.CharField(max_length=60, blank=False) 
    password=models.CharField(max_length=30, blank=False)
    email=models.EmailField(blank=False)

class Materia(models.Model):
    #enlace id con user
    user = models.ForeignKey(Register, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30, blank = False)
    hora = models.TimeField(blank = False)
    profesor = models.CharField(max_length = 30, blank = False)
    profesor_email = models.EmailField(blank = False)
    def __str__(self):
        return self.name
    #UNAL vs NO UNAL

class Seccion(models.Model):
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



    