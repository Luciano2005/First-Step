# -*- coding: utf-8 -*-
from ast import MatchSequence
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.conf.global_settings import MEDIA_ROOT
from django.contrib import messages
import pathlib
import os
from django.conf import settings
from urllib.parse import unquote, quote
from ESTUDIO.models import Pregunta
from .forms import Registro, Loguearse, newMateria, newSeccion, newTarea, newDocumento, editUser,editPassword
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .models import Materia, Seccion, Tarea, Documento
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import PasswordResetTokenGenerator, account_activation_token
from pprint import pprint
from Google import Create_Service, get_token, convert_to_RFC_datetime
import datetime
# Create your views here.
#---------------------------------------------------Login y Register-----------------------------------------

def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html',{
            'form':Registro
    })
    else:
        if request.POST['g-recaptcha-response'] != '':
            if User.objects.filter(email = request.POST['email']).exists():
                return render(request, 'register.html',{
                    'form':Registro,
                    'error':'El correo que está usando ya existe'
                    })  
            else:    
                if request.POST['password1']==request.POST['password2']: 
                    try:
                        user=User.objects.create_user(username=request.POST['username'],first_name=request.POST['first_name'],email=request.POST['email'],password=request.POST['password1']) 
                        user.is_active=False
                        user.save()
                        #ENVIAR EMAIL. AQUÍ LO QUE SE HACE ES COLOCAR QUIÉN MANDA EL CORREO, A DÓNDE LO MANDA Y LO QUE DICE
                        uidb64=(urlsafe_base64_encode(force_bytes(user.pk)))

                        email=request.POST['email']
                        domain= get_current_site(request).domain
                        link=reverse('verificar',kwargs={'uidb64':uidb64,'token':account_activation_token.make_token(user)})
                        url_activacion='http://'+domain+link
                        email_subject='Active su cuenta'
                        email_body='¡Hola, '+user.username+ ' esperamos estés bien. Para activar tu cuenta correctamente, por favor presiona el siguiente link '+url_activacion
                        email= EmailMessage(
                            email_subject,
                            email_body,
                           'firststepunal@gmail.com',
                            [email],
                        )
                        email.send(fail_silently=False)
                        messages.success(request,"CUENTA A VERIFICAR")
                        login(request, user)
                        return redirect("login")
                    except IntegrityError:
                        return render(request, 'register.html',{
                            'form':Registro,
                            'error':'El nombre de usuario que registró, ya existe'
                            })
                    except ValueError:
                        return render(request, 'register.html',{
                    'form':Registro,
                    'error':'Existe por lo menos un campo sin completar'
            })
            return render(request, 'register.html',{
                'form':Registro,
                'error':'Las contraseñas no coindicen'
            })
        else:
            return render(request, 'register.html',{
                'form':Registro,
                'error':'Verifique el CAPTCHA'
            }) 

#TOKEN
def verificar(request, uidb64, token):
    try:
        id=force_str(urlsafe_base64_decode(uidb64))
        user= User.objects.get(pk=id)
        if not account_activation_token.check_token(user, token):
            return redirect('login'+'?message='+'Usario ACTIVO')
        if user.is_active:
            return redirect('login')
        user.is_active=True
        user.save()
        messages.success(request,'CUENTA ACTIVADA')
        return redirect('login')
    except Exception as ex:
        pass
    return redirect('login')

def formlogin(request):
    if request.method== 'GET':
        return render(request, 'login.html',{
            'form':Loguearse
    })
    else:
        if request.POST['g-recaptcha-response'] != '':
            user= authenticate(request, username=request.POST['username'],password=request.POST['password'])
            if user is None:
                consulta_user = User.objects.filter(username=request.POST['username'])
                # print(consulta_user[0].is_active)
                if len(consulta_user) > 0 and consulta_user[0].is_active==False:
                    return render(request, 'login.html',{
                    'form':Loguearse,
                    'error':'No has verificado tu cuenta. Por favor ingresa a tu correo.'})
                return render(request, 'login.html',{
                    'form':Loguearse,
                    'error':'Nombre de usuario o contraseña incorrecto'
                    })
            else:
                login(request, user)
                return redirect('main')
        else:
            return render(request, 'login.html',{
                    'form':Loguearse,
                    'error':'Verifique el CAPTCHA'
                    }) 

@login_required
def logout2(request):
    #os.remove(os.path.join('token files/token_calendar_v3.pickle'))
    global s
    s=False
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    return render(request, 'perfil.html')


#---------------------------------------------------Materias-----------------------------------------

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
        print(request.POST)
        print(request.FILES)
        if 'imagen' in request.POST:
            if materia.imagen != '' and 'imagen-clear' in request.POST and request.POST['imagen-clear']=='on':
                image_path = materia.imagen.path
                if os.path.exists(image_path):
                    os.remove(image_path)
            form = newMateria(request.POST, instance=materia)
            # Materia.objects.filter(id = materia.id).update(user=request.user, name=request.POST['name'], hora=request.POST['hora'], profesor=request.POST['profesor'], profesor_email=request.POST['profesor_email'], horario=request.POST.getlist('horario'), aula=request.POST['aula'])
            form.save()
        else:
            
            if materia.imagen != '':
                image_path = materia.imagen.path
                if os.path.exists(image_path):
                    os.remove(image_path)
            if 'imagen-clear' in request.POST and request.POST['imagen-clear']=='on':
                envio = request.POST.copy()
                envio.pop('imagen-clear')
                print(envio)
                form = newMateria(envio, request.FILES, instance=materia)
                form.save()
            else:
                form = newMateria(request.POST, request.FILES, instance=materia)
                form.save()
            # Materia.objects.filter(id = materia.id).update(user=request.user, name=request.POST['name'], hora=request.POST['hora'], profesor=request.POST['profesor'], profesor_email=request.POST['profesor_email'], horario=request.POST.getlist('horario'), imagen=request.FILES['imagen'], aula=request.POST['aula'])

        return redirect('materias')

@login_required
def elmimiarMateria(request, materia_id):
    if request.method == 'POST':
        archivos = list(Documento.objects.filter(user=request.user,materia_id=materia_id))
        for archivo in archivos:
            os.remove(os.path.join('.'+MEDIA_ROOT+archivo.documento.url))
        materia = get_object_or_404(Materia, pk=materia_id, user=request.user)
        materia.delete()
        return redirect('materias')

@login_required
def crearMateria(request):
    
    if request.method == 'GET':
        return render(request, 'crearMateria.html', {
        'form' : newMateria(),
        'docForm' : newDocumento(),
    })
    else:
        #try:
        print(request.FILES)
        # form= newMateria(request.POST)
        # new_materia=form.save(commit=False)
        # new_materia.user=request.user


        #new_materia.save()
        if 'imagen' in request.POST:
            materia = Materia.objects.create(user=request.user, name=request.POST['name'], hora=request.POST['hora'], profesor=request.POST['profesor'], profesor_email=request.POST['profesor_email'], horario=request.POST.getlist('horario'), aula=request.POST['aula'])
        else:
            materia = Materia.objects.create(user=request.user, name=request.POST['name'], hora=request.POST['hora'], profesor=request.POST['profesor'], profesor_email=request.POST['profesor_email'], horario=request.POST.getlist('horario'), imagen=request.FILES['imagen'],aula=request.POST['aula'])

        materia.save()
        for doc in request.FILES.getlist('documento'):
            Documento.objects.create(user = request.user, documento = doc, materia = materia)
         
        

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



#---------------------------------------------------Crear Sección-----------------------------------------

@login_required
def crearSeccion(request, materia_id):
    if request.method == 'GET':
        return render(request, 'crearSeccion.html', {
            'form' : newSeccion()
        })
    else:
        Seccion.objects.create(user = request.user, name = request.POST['name'], materia_id = materia_id)    
        return redirect('materia_detail', materia_id)

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
        return redirect('materia_detail', seccion.materia_id)
        
@login_required
def eliminarSeccion(request, seccion_id):
    if request.method=='POST':
        seccion = get_object_or_404(Seccion, pk=seccion_id, user=request.user)
        seccion.delete()
        return redirect('materia_detail', seccion.materia_id)

#---------------------VISTA TAREAS------------------------------------------------

@login_required
def mostrarTareas(request):
    prioridadA= Tarea.objects.filter(user=request.user,prioridad='Alto').order_by('fecha')
    prioridadM= Tarea.objects.filter(user=request.user,prioridad='Medio').order_by('fecha')
    prioridadB= Tarea.objects.filter(user=request.user,prioridad='Bajo').order_by('fecha')
    return render(request, 'mostrarTareas.html',{
        'tareas_a':prioridadA,
        'tareas_m':prioridadM,
        'tareas_b':prioridadB,

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
        if request.POST['fecha'] != '' :
            Tarea.objects.create(user = request.user, name = request.POST['name'], materia_id = request.POST['materia'], prioridad = request.POST['prioridad'], fecha = request.POST['fecha'])
        else:
            Tarea.objects.create(user = request.user, name = request.POST['name'], materia_id = request.POST['materia'], prioridad = request.POST['prioridad'])
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



#---------------------------------------------------Archivos-----------------------------------------
def verArchivos(request, materia_id):
    if request.method == 'GET':
        lista_archivos=list(Documento.objects.filter(user=request.user, materia_id=materia_id))
        return render(request, 'verArchivos.html',{
            'archivos':lista_archivos,
            'materia_id':materia_id,
            'agregar':newDocumento()
        })

def eliminarArchivo(request, archivo_id):
    archivo=get_object_or_404(Documento,user=request.user, pk=archivo_id)
    materia_id=archivo.materia.id
    os.remove(os.path.join('.'+MEDIA_ROOT+unquote(archivo.documento.url)))
    archivo.delete()
    return redirect('verArchivos', materia_id)

def agregarArchivos(request, materia_id):
    for doc in request.FILES.getlist('documento'):
        Documento.objects.create(user = request.user, documento = doc, materia_id = materia_id)
    return redirect('verArchivos', materia_id)



    
#-------------------------------------------------Mi Perfil-------------------------------------------------
def perfil(request):
    if request.method=='GET':
        form=editUser(instance=request.user)
        cambiar_contrasena=editPassword(request.user)
        return render(request, 'perfil.html',{
            'form':form,
            'cambiar_contrasena':cambiar_contrasena
        })
    else:
        form=editUser(request.POST, instance=request.user)

        # messages.success(request,"HAS CAMBIADO TU USUARIO")
        cambiar_contrasena=editPassword(request.user, request.POST)
        if request.POST['new_password1']==request.POST['new_password2'] and request.POST['old_password'] != request.POST['new_password1'] and len(request.POST['new_password1']) != 0:
            if cambiar_contrasena.is_valid():
                # new_password1_id=cambiar_contrasena.cleaned_data['new_password1']
                user=cambiar_contrasena.save()
                update_session_auth_hash(request, user)
                form.save()
                # messages.success(request,"HAS CAMBIADO TU CONTRASEÑA EXITOSAMENTE")
            else:
                return render(request, 'perfil.html',{
                    'form':form,
                    'cambiar_contrasena':cambiar_contrasena,
                })
            return redirect('perfil')
        else:
        #     messages.error(request,"Las contraseñas es muy corta")
            if (request.POST['username']!=request.user.username or request.POST['email']!=request.user.email) and not User.objects.filter(email = request.POST['email']).exists():
                try:
                    form.save()
                    return redirect('materias')
                except ValueError:
                    pass
            if User.objects.filter(email = request.POST['email']).exists() and request.POST['email']!=request.user.email :
                return render(request, 'perfil.html',{
                    'form':form,
                    'cambiar_contrasena':cambiar_contrasena,
                    'error':'El correo que está usando ya existe'
                    })
            return render(request, 'perfil.html',{
                'form':form,
                'cambiar_contrasena':cambiar_contrasena,
            })


#-------------------------------------------Calendar----------------------------------------------------------------
service=None
s=False
id_calendario=''

def calendar(request):
    global s, service, id_calendario
    if request.method == 'POST':
        if s==False:
            s=solicitud_calendar(request)
            if s==True:
                
                response=service.calendarList().list().execute()
                calendarItems=response.get('items')
                myCalendar=filter(lambda x:'First-Step' in x['summary'], calendarItems)
                myCalendar=next(myCalendar)
                calendar_id_firststep=myCalendar['id']
                id_calendario=quote(calendar_id_firststep)
                
                rules = {
                    "role": "reader",
                    "scope": {
                        "type": "default",
                    }
                    }
                created_rule = service.acl().insert(calendarId=calendar_id_firststep, body=rules).execute()
        else:
            # Consultar calendario
            response=service.calendarList().list().execute()
            calendarItems=response.get('items')
            myCalendar=filter(lambda x:'First-Step' in x['summary'], calendarItems)
            myCalendar=next(myCalendar)
            calendar_id_firststep=myCalendar['id'] #Id del calendario
            id_calendario=quote(calendar_id_firststep)
            #Fecha y hora del  evento
            date_start= request.POST['datetime-start'][:10].split('-')
            time_start=request.POST['datetime-start'][11:].split(':')
            date_end=request.POST['datetime-end'][:10].split('-')
            time_end=request.POST['datetime-end'][11:].split(':')
            #Crear evento
            hour_adjustment=5
            event_request_body={
                'start':{
                    'dateTime':convert_to_RFC_datetime(int(date_start[0]),int(date_start[1]),int(date_start[2]),int(time_start[0])+hour_adjustment,0 if int(time_start[1])<30 else 30),
                    'timeZone':'America/Bogota'
                },
                'end':{
                    'dateTime':convert_to_RFC_datetime(int(date_end[0]),int(date_end[1]),int(date_end[2]),int(time_end[0])+hour_adjustment,0 if int(time_end[1])<30 else 30) ,
                    'timeZone':'America/Bogota'
                },
                'summary':request.POST['title'],
                'description':request.POST['description'],
                'colorId':5,
                'status':'confirmed',
                'transparency': 'opaque',
                'visibility': 'public',
                # 'creator':{

                # },
                # 'organizer':{
                    
                # }
            }
            sendNotification=True
            sendUpdate='none'
            response=service.events().insert(
                calendarId=calendar_id_firststep,
                sendNotifications=sendNotification,
                sendUpdates=sendUpdate,
                body=event_request_body

            ).execute()
            return render(request, 'calendar.html',{
                'verifica':s,
                'enviado':'Evento creado exitosamente',
                'calendario': id_calendario
            })
    else:
        return render(request, 'calendar.html',{
            'verifica':s,
            'calendario': id_calendario
        })
    return redirect('calendar')

def solicitud_calendar(request,):
    CLIENT_SECRET_FILE = 'client_secret_883464149952-j83ui7qf98nsu8o1q8jbir4aacqv80gq.apps.googleusercontent.com.json'
    API_NAME = 'calendar'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    global service
    service = Create_Service(request.user,CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    #Consultar si el calendario existe
    response=service.calendarList().list().execute()
    calendarItems=response.get('items')
    myCalendar=filter(lambda x:'First-Step' in x['summary'], calendarItems)
    # print(myCalendar)
    try:
        myCalendar=next(myCalendar)
        id_calendario=quote(myCalendar['id'])
    except:
        request_body={
            'summary': 'First-Step', #Titulo del calendario
            'description':'Organización y productividad'
        }
        response= service.calendars().insert(body=request_body).execute()
        print("Deberia Funcionar")

    # if myCalendar==None:
        #Cuerpo del nuevo calendario
    

    # #Crear Nuevo calendario
    

    #Listar todos los calendarios del usuario
    # response=service.calendarList().list().execute()
    # pprint(response)

    # calendarItems=response.get('items') #Obtener los items de cada calendario
    # myCalendar=filter(lambda x:'Nuevo calendario con la API :D' in x['summary'], calendarItems) #Filtrar para actualizar
    # myCalendar=next(myCalendar)
    # print(myCalendar) #Imprime en consola

    #Actualizaciones
    # myCalendar['summary'] = 'First-Step'
    # myCalendar['description'] = 'Este es un nuevo calendario creado con API calendar'
    # myCalendar['location'] = 'Neiva, Huila'

    #Ejecuta actualizaciones
    # service.calendars().update(calendarId=myCalendar['id'], body=myCalendar).execute()
    return True
    # guardarUser(request)
    

# def guardarUser(request):
#     Calendar.objects.create(user=request.user, key=get_token())
    
        



