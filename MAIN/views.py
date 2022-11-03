from ast import MatchSequence
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from ESTUDIO.models import Pregunta
from .forms import Registro, Loguearse, newMateria, newSeccion, newTarea, newDocumento
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Materia, Seccion, Tarea, Documento

# Create your views here.
docs = []

def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html',{
            'form':Registro
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
def materias(request):
    materias = Materia.objects.filter(user = request.user)
    return render(request, 'materias.html', {
        'materias' : materias
    })

@login_required
def materia_detail(request, materia_id):
        materia = get_object_or_404(Materia, pk=materia_id,user=request.user)
        form=newMateria(instance=materia)
        seccion = list(Seccion.objects.filter(user= request.user, materia=materia_id))
        return render(request, 'materia_detail.html', {
            'materia' : materia,
            'form':form,
            'seccions' : seccion
        })
        #Manejar para cuando no hayan secciones creadas

@login_required
def cambiarMateria(request, materia_id):
    if request.method == 'GET':
        materia = get_object_or_404(Materia, pk=materia_id)
        form=newMateria(instance=materia)
        return render(request, 'cambiarMateria.html' , {
            'form' : form
        })
    else:
        materia = get_object_or_404(Materia, pk=materia_id, user=request.user)
        Materia.objects.filter(id = materia.id).update(user=request.user, name=request.POST['name'], hora=request.POST['hora'], profesor=request.POST['profesor'], profesor_email=request.POST['profesor_email'], horario=request.POST.getlist('horario'))
        return redirect('materias')

@login_required
def elmimiarMateria(request, materia_id):
    if request.method == 'POST':
        materia = get_object_or_404(Materia, pk=materia_id, user=request.user)
        materia.delete()
        return redirect('materias')

@login_required
def crearMateria(request):
    global docs
    if request.method == 'GET':
        return render(request, 'crearMateria.html', {
        'form' : newMateria(),
        'docForm' : newDocumento(),
        'docs' : docs
    })
    else:
        #try:
        print(request.POST)
        # form= newMateria(request.POST)
        # new_materia=form.save(commit=False)
        # new_materia.user=request.user


        #new_materia.save()

        materia = Materia.objects.create(user=request.user, name=request.POST['name'], hora=request.POST['hora'], profesor=request.POST['profesor'], profesor_email=request.POST['profesor_email'], horario=request.POST.getlist('horario'), imagen=request.FILES['imagen'])
        materia.save()
        for doc in request.FILES.getlist('documento'):
            a = Documento.objects.create(user = request.user, documento = doc, materia = materia)
         
        docs = []

        return redirect('/materias/')
        # except ValueError:
        #     global x
        #     a = request.POST['profesor_email']
        #     if a.find(".") == -1:
        #         x = "Correo Invalido"
        #     else:
        #         if len(a.split(".")[1]) == 1:
        #             x = "Correo Invalido"
        #         else:
        #             x = "Eror en hora o en otra cosa diferente a correo"

        #     return render(request,'crearMateria.html',{
        #         'form':newMateria,
        #         'error': x
        #     })

@login_required
def crearSeccion(request, materia_id):
    if request.method == 'GET':
        return render(request, 'crearSeccion.html', {
            'form' : newSeccion()
        })
    else:
        Seccion.objects.create(user = request.user, name = request.POST['name'], materia_id = materia_id)    
        return redirect('/materias/')

@login_required
def seccion_detail(request, seccion_id):
    seccion=get_object_or_404(Seccion,pk=seccion_id,user=request.user)
    pregunta = list(Pregunta.objects.filter(seccion_id=seccion_id, user = request.user))
    
    return render(request, 'seccion_detail.html',{
        'seccion':seccion,
        'preguntas':pregunta
    } )
    
@login_required
def cambiarSeccion(request, seccion_id):
    if request.method=='GET':
        seccion=get_object_or_404(Seccion,pk=seccion_id,user=request.user)
        form=newSeccion(instance=seccion)
        return render(request,'cambiarSeccion.html',{
            'form':form
        })
    else:
        seccion=get_object_or_404(Seccion,pk=seccion_id,user=request.user)
        form=newSeccion(request.POST,instance=seccion)
        form.save()
        return redirect('materias')
        
@login_required
def eliminarSeccion(request, seccion_id):
    if request.method=='POST':
        seccion = get_object_or_404(Seccion, pk=seccion_id, user=request.user)
        seccion.delete()
        return redirect('materias')

#---------------------VISTA TAREAS------------------------------------------------

@login_required
def mostrarTareas(request):
    prioridadA= Tarea.objects.filter(user=request.user,prioridad='Alto').order_by('fecha')
    prioridadM= Tarea.objects.filter(user=request.user,prioridad='Medio').order_by('fecha')
    prioridadB= Tarea.objects.filter(user=request.user,prioridad='Bajo').order_by('fecha')

    return render(request, 'mostrarTareas.html',{
        'tareas_a':prioridadA,
        'tareas_m':prioridadM,
        'tareas_b':prioridadB
    })


@login_required
def tarea_detail(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id,user=request.user)
    return render(request, 'tarea_detail.html', {
       'tarea':tarea
    })

def crearTarea(request):
    if request.method == 'GET':
        #tarea=newTarea()

        return render(request, 'crearTarea.html', {
            'form' : newTarea(user=request.user)
        })
    else:
        form= newTarea(request.POST)
        new_tarea=form.save(commit=False)
        new_tarea.user=request.user
        new_tarea.save()
        return redirect('/tareas/')

@login_required
def actualizarTarea(request, tarea_id):
    if request.method=='GET':
        tarea=get_object_or_404(Tarea,pk=tarea_id)
        form=newTarea(user=request.user,instance=tarea)
        return render(request, 'actualizarTarea.html',{
            'form':form
        })
    else:
        tarea=get_object_or_404(Tarea,pk=tarea_id,user=request.user)
        form=newTarea(request.POST, instance=tarea)
        form.save()
        return redirect('/tareas/')

@login_required
def eliminarTarea(request, tarea_id):
    if request.method=='POST':
        tarea=get_object_or_404(Tarea, pk=tarea_id, user=request.user)
        print(tarea.name)
        tarea.delete()
        return redirect('/tareas/')

@login_required
def crearDoc(request):
    global docs
    docs.append(newDocumento())
    print(len(docs))
    return redirect('crearMateria')