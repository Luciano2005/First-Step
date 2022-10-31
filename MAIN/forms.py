from time import time
from django import forms
from django.forms import ModelForm, Widget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from MAIN.models import Materia, Seccion, Tarea

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
        widgets = {
            'username' : forms.TextInput(attrs=({'placeholder':'Username/tagname/apodo', 'class':'form-control'})),
            'first_name' : forms.TextInput(attrs=({'placeholder':'Primer nombre', 'class':'form-control'})),
            'email' : forms.TextInput(attrs=({'placeholder':'name@unal.edu.co', 'class':'form-control'})),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput()
        } 

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
        widgets={
            'username' : forms.TextInput(attrs=({'placeholder':'Username/tagname/apodo', 'class':'form-control'}))
        }

class newMateria(forms.ModelForm):
    class Meta:
        model=Materia
        fields=['name','hora','profesor','profesor_email']
        widgets = {
            'name' : forms.TextInput(attrs=({'placeholder':'Nombre de la materia', 'class':'form-control'})),
            'profesor' : forms.TextInput(attrs=({'placeholder':'Nombre del profesor', 'class':'form-control'})),
            'profesor_email' : forms.TextInput(attrs=({'placeholder':'name@unal.edu.co', 'class':'form-control'})),
            'hora' : forms.TimeInput(attrs=({'type':'time'})),
        } 

class newSeccion(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = ['name']

class newTarea(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user', None)
       super().__init__(*args, **kwargs)
       if user:
           self.fields['materia'].queryset = Materia.objects.filter(user=user)
    class Meta:
        model = Tarea
        fields = ['name','materia','prioridad','fecha']
