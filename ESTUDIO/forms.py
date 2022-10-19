from django import forms
from ESTUDIO.models import Pregunta

class newPregunta(forms.ModelForm):
    class Meta:
        model=Pregunta
        fields=['name','respuesta','apropiacion','ultima_vez','seccion']
