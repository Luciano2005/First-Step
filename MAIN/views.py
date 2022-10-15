from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Registro
from django.contrib.auth.models import User

# Create your views here.

def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html',{
            'forms':Registro
    })
    else:
        if request.POST['password1']==request.POST['password2']: 
            try:
                user=User.objects.create_user(username=request.POST['username'],first_name=request.POST['first_name'],email=request.POST['email'],password=request.POST['password1']) 
                user.save()
                return redirect("login")
            except IntegrityError:
                return render(request, 'register.html',{
                    'forms':Registro,
                    'error':'El nombre de usuario que registró, ya existe'
                    })
            except ValueError:
                return render(request, 'register.html',{
            'forms':Registro,
            'error':'Existe por lo menos un campo sin completar'
    })
        return render(request, 'register.html',{
            'forms':Registro,
            'error':'Las contraseñas no coindicen'
    })

def login(request):
    return render(request, 'login.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')
