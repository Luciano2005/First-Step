from django import forms
from django.forms import ModelForm
from ESTUDIO.models import Pregunta, RespuestasCerradas
from django.forms.widgets import HiddenInput

class newPregunta(forms.ModelForm):
    class Meta:
        model=Pregunta
        fields=['name','respuesta','apropiacion','ultima_vez','seccion']
        widgets = {
            'apropiacion' : HiddenInput(),
            'ultima_vez' : HiddenInput(),
            'seccion' : HiddenInput()
        } 

class newRespuestaCerrada(forms.ModelForm):
    class Meta:
        model=RespuestasCerradas
        fields=['respuesta_cerrada']
