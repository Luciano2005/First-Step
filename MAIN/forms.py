from time import time
from django import forms
from django.forms import ModelForm, Widget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from MAIN.models import Materia, Seccion

class Registro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Nombre de usuario'
        self.fields['first_name'].label='Nombre'
        self.fields['first_name'].required=True
        self.fields['email'].label='Email'
        self.fields['email'].required=True
        self.fields['password1'].label='Contraseña'
        self.fields['password2'].label='Confirmar Contraseña'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model=User
        fields=['username','first_name','email','password1','password2']

class Loguearse(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Nombre de usuario'
        self.fields['password'].label='Contraseña'
        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None
            
    class Meta:
        model=User
        fields=['username','password']

class newMateria(forms.ModelForm):
    class Meta:
        model=Materia
        fields=['name','hora','profesor','profesor_email']
        widgets = {
            'name' : forms.TextInput(attrs=({'placeholder':'Nombre de la materia', 'class':'form-control'})),
            'profesor' : forms.TextInput(attrs=({'placeholder':'Nombre del profesor', 'class':'form-control'})),
            'profesor_email' : forms.EmailInput(attrs=({'placeholder':'name@unal.edu.co', 'class':'form-control'})),
            'hora' : forms.TimeInput(attrs=({'type':'time'})),
        } 

class newSeccion(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = ['name']

