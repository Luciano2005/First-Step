from django import forms
from ESTUDIO.models import Pregunta
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
