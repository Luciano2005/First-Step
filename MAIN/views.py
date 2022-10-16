from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Registro, Loguearse, newMateria
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Materia
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
                login(request, user)
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

def formlogin(request):
    if request.method== 'GET':
        return render(request, 'login.html',{
            'form':Loguearse
    })
    else:
        user= authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
         return render(request, 'login.html',{
            'form':Loguearse,
            'error':'Nombre de usuario o contraseña incorrecto'
            }) 
        else:
            login(request, user)
            return redirect('main')

@login_required
def logout2(request):
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def crearMateria(request):
    if request.method == 'GET':
        return render(request, 'crearMateria.html', {
        'form' : newMateria()
    })
    else:
        Materia.objects.create(name = request.POST['name'], hora = request.POST['hora'], profesor = request.POST['profesor'], profesor_email = request.POST['profesor_email'])
        return redirect('/perfil/')

@login_required
def flashcard(request):
    return render(request,'flashcard.html')

