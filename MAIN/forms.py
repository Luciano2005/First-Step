from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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

class newMateria(forms.Form):
    name = forms.CharField(label = "Nombre de la materia", required = True)
    hora = forms.TimeField(label = "Hora de inicio de la materia", required = True)
    profesor = forms.CharField(label = "Nombre del profesor", required = True)
    profesor_email = forms.EmailField(label = "Correo del profesor", required = True)

