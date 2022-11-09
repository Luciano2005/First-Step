from time import time
from django import forms
from django.forms import ModelForm, Widget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from MAIN.models import Materia, Seccion, Tarea, Documento

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
        fields=['name','hora','profesor','profesor_email','horario', 'aula','imagen']
        widgets = {
            'name' : forms.TextInput(attrs=({'placeholder':'Nombre de la materia', 'class':'form-control'})),
            'profesor' : forms.TextInput(attrs=({'placeholder':'Nombre del profesor', 'class':'form-control'})),
            'profesor_email' : forms.TextInput(attrs=({'placeholder':'name@unal.edu.co', 'class':'form-control'})),
            'hora' : forms.TimeInput(attrs=({'type':'time'}))
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

class newDocumento(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['documento']
        widgets={
            'documento':forms.FileInput(attrs={'multiple': True})
        }

class editUser(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Nombre de usuario'
        self.fields['email'].label='Email'
        self.fields['email'].required=True
        for fieldname in ['username']:
            self.fields[fieldname].help_text = None
    class Meta:
        model=User
        fields=['username', 'email']

class editPassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label='Contraseña antigua'
        self.fields['new_password1'].label='Nueva contraseña'
        self.fields['new_password2'].label='Confirma contraseña'
        self.fields['old_password'].required=False
        self.fields['new_password1'].required=False
        self.fields['new_password2'].required=False
        for fieldname in ['new_password1','new_password2','old_password']:
            self.fields[fieldname].help_text = None
            
    # def clean_new_password1(self):
    #     data = self.cleaned_data['new_password1']
    #     if len(data) < 8 or len(data) > 64:
    #         raise editPassword.ValidationError("New password should have minimum 8 characters and maximum 64 characters")
    #     return data
    def clean_old_password(self):
        try:
            return super(editPassword, self).clean_old_password()
        except forms.ValidationError:
            raise forms.ValidationError("La contraseña ingresada no es la correcta")

    # def clean_new_password1(self):
    #     data = self.cleaned_data['new_password1']
    #     if len(data) == 0:
    #         raise forms.ValidationError("New password should have minimum 8 characters and maximum 64 characters")
    #     return data
    
    def clean_new_password2(self):
        try:
            return super(editPassword, self).clean_new_password2()
        except forms.ValidationError:
            raise forms.ValidationError("Las contraseñas no son iguales o la nueva contraseña no tiene minimo 8 caracteres diferentes")
            


    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']