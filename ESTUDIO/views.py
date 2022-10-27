from doctest import FAIL_FAST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import QueryDict
from django.urls import reverse

from ESTUDIO.forms import newPregunta,newRespuestaCerrada,newPreguntaCerrada,newRespuestaCerradaVerdadera
from ESTUDIO.models import Pregunta,RespuestasCerradas
from MAIN.models import Seccion
from MAIN.forms import newSeccion

# Create your views here.
respuestas=[] #Lista para guardar las respuestas cerradas que el usuario ingresa.
@login_required
def crearFlashcard(request, seccion_id):
    global respuestas
    if request.method == 'GET':
        return render(request, 'crearFlashcard.html', {
            'form_pregunta' : newPregunta(), #Formulario de nueva pregunta
            'seccion': seccion_id, #Pasamos seccion_id para que no haya error en la funcion de crearRespuestaCerrada
        })
    else:
        Pregunta.objects.create(user = request.user, name = request.POST['name'], respuesta = request.POST['respuesta'], apropiacion = 1, seccion_id = seccion_id) #Se crea una nueva pregunta
        
        
    
        return redirect('/materias/')

@login_required
def crearPreguntaCerrada(request, seccion):
    global respuestas #Usamos la lista para guardar los nuevos campos de respuestas cerradas.
    if request.method=='GET':
        return render(request, 'crearPreguntaCerrada.html',{
            'form_pregunta_cerrada' : newPreguntaCerrada(),
            'seccion':seccion,
            'respuestas':respuestas,
            'respuesta_verdadera': newRespuestaCerradaVerdadera()
        })
    else:
        pregunta=Pregunta.objects.create(user = request.user, name = request.POST['name'], respuesta = request.POST['respuesta'], apropiacion = 1, seccion_id = seccion) #Se crea una nueva pregunta
        pregunta.save()
        
        for respuesta in request.POST.getlist('respuesta_cerrada'): #Recorremos las respuestas cerradas.
            RespuestasCerradas.objects.create(user=request.user, respuesta_cerrada=respuesta, pregunta=pregunta, respuesta_verdadera=request.POST['respuesta_verdadera']) #Guardamos cada respuesta.

        respuestas=[] #Reiniciamos la lista de respuestas cerradas
        
        return redirect('/materias/')
    



@login_required
def crearRespuestaCerrada(request, seccion):
    global respuestas #Usamos la lista para guardar los nuevos campos de respuestas cerradas.
    respuestas.append(newRespuestaCerrada()) #Agregamos el formulario de respuestas.
    print(len(respuestas)) #Verificamos que se esten guardando las respuestas BORRAR LINEA.
    return redirect('estudio:crearPreguntaCerrada', seccion)

@login_required
def eliminarRespuestaCerrada(request, seccion):
    global respuestas
    if len(respuestas)>1:
        respuestas.pop() #eliminamos el último formulario de respuestas agregado.
        print(len(respuestas)) #Verificamos que se esten borrando las respuestas BORRAR LINEA.
    return redirect('estudio:crearPreguntaCerrada', seccion) #Devolvemos la vista con el nuevo campo de respuesta cerrada.

@login_required
def pregunta_detail(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, user = request.user, pk = pregunta_id)
    return render(request, 'pregunta_detail.html', {
        'pregunta' : pregunta
    })

#-----------------------------PUEDE SERVIR PARA EL FUTURO------------------------------------------------
# @login_required
# def pregunta_cerrada_detail(request, pregunta_id):
#     pregunta = get_object_or_404(Pregunta, user = request.user, pk = pregunta_id)
#     respuestas= get_list_or_404(RespuestasCerradas, user=request.user, respuesta_cerrada=respuestas, pregunta_id=pregunta_id)
#     print(respuestas)
#     return render(request, 'pregunta_detail.html', {
#         'pregunta' : pregunta
#     })
@login_required
def redireccionarPregunta(request, pregunta_id):
    respuestas = list(RespuestasCerradas.objects.filter(user=request.user, pregunta_id=pregunta_id))
    if len(respuestas):
        return redirect('estudio:pregunta_cerrada', pregunta_id)
    else:
        return redirect('estudio:cambiarPregunta', pregunta_id)

@login_required
def cambiarPregunta(request, pregunta_id):
    if request.method == 'GET':
        pregunta = get_object_or_404(Pregunta, user = request.user, pk = pregunta_id)
        form = newPregunta(instance=pregunta)
        return render(request, 'cambiarPregunta.html', {
            'form' : form
        })
    else:
        pregunta = get_object_or_404(Pregunta, user = request.user, pk = pregunta_id)
        form = newPregunta(request.POST, instance=pregunta)       
        form.save()
        return redirect('/materias/') 


@login_required
def cambiarPreguntaCerrada(request, pregunta_id, size=None, eliminar=None):
    form_respuesta=[]
    if request.method == 'GET':
        pregunta = get_object_or_404(Pregunta, user = request.user, pk = pregunta_id)
        lista_respuestas = get_list_or_404(RespuestasCerradas, user=request.user, pregunta_id=pregunta_id)
        form_pregunta = newPreguntaCerrada(instance=pregunta)
        respuesta_verdadera = newRespuestaCerradaVerdadera(instance=lista_respuestas[0])
        for respuesta in lista_respuestas:
            form_respuesta.append(newRespuestaCerrada(instance=respuesta))
        
        if size==None:
            size=0
        if eliminar==None:
            eliminar=0

        lista_nuevas_respuestas=[]
        for i in range(0,size):
            lista_nuevas_respuestas.append(newRespuestaCerrada())

        
        return render(request, 'cambiarPregunta.html', {
            'form_pregunta' : form_pregunta,
            'form_respuesta' : form_respuesta,
            'respuesta_verdadera': respuesta_verdadera,
            'pregunta':pregunta,
            'nueva_respuesta':lista_nuevas_respuestas,
            'size':size+1,
            'eliminar':size-1
        })
        
    else:
        pregunta = get_object_or_404(Pregunta, user = request.user, pk = pregunta_id)
        respuestas = get_list_or_404(RespuestasCerradas, user=request.user,pregunta_id=pregunta_id)
        form_pregunta = newPreguntaCerrada(request.POST, instance=pregunta)
        form_pregunta.save()

        n=request.POST.getlist('respuesta_cerrada')

        for respuesta in respuestas:
            RespuestasCerradas.objects.filter(pk=respuesta.id,user=request.user,pregunta_id=pregunta_id).update(respuesta_cerrada=n.pop(0), respuesta_verdadera=request.POST['respuesta_verdadera'])        
            
        return redirect('/materias/') 

# @login_required
# def crearMasRespuestasCerradas(request, pregunta_id):
#     global respuestas #Usamos la lista para guardar los nuevos campos de respuestas cerradas.
#     respuestas.append(newRespuestaCerrada()) #Agregamos el formulario de respuestas.
#     print(len(respuestas)) #Verificamos que se esten guardando las respuestas BORRAR LINEA.
#     return redirect('estudio:pregunta_cerrada', pregunta_id)        

@login_required
def eliminarPregunta(request, pregunta_id):
    if request.method == 'POST':
        pregunta=get_object_or_404(Pregunta, user=request.user, pk=pregunta_id)
        pregunta.delete()
        return redirect('/materias/')

contador=0
preguntas=[]
@login_required
def repasoFlashcard(request, seccion_id):
    global contador 
    global preguntas
    preguntas = crearPreguntas(request, seccion_id, contador, preguntas)
    if request.method == 'GET':
           
        contador+=1
        seccion=get_object_or_404(Seccion,pk=seccion_id,user=request.user)
        
        try:
            respuestas_cerradas=RespuestasCerradas.objects.filter(user=request.user,pregunta=preguntas[contador-1]).order_by('?')
            return render(request, 'repaso.html',{
                'pregunta':preguntas[contador-1],
                'seccion':seccion,
                'respuestas_cerradas':respuestas_cerradas
                })
        except IndexError:
            contador=0
            return redirect('/materias/')
    else:
        seccion=get_object_or_404(Seccion,pk=seccion_id,user=request.user)
        respuestas_cerradas=RespuestasCerradas.objects.filter(user=request.user,pregunta=preguntas[contador-1])
        print(respuestas_cerradas)
        try:
            return render(request, 'repaso.html',{
                    'pregunta':preguntas[contador-1],
                    'seccion':seccion,
                    'respuesta':preguntas[contador-1].respuesta,
                    'respuestas_cerradas':respuestas_cerradas,
                    'verdadera':respuestas_cerradas[0].respuesta_verdadera
                    })
        except IndexError:
            return render(request, 'repaso.html',{
                    'pregunta':preguntas[contador-1],
                    'seccion':seccion,
                    'respuesta':preguntas[contador-1].respuesta,
                    'respuestas_cerradas':respuestas_cerradas,
                    #'verdadera':respuestas_cerradas[0].respuesta_verdadera
                    })
        
@login_required     
def crearPreguntas(request, seccion_id, contador, preguntas): #Crear lita de preguntas organizadas de forma aleatoria
    if contador==0:
        preguntas=list(Pregunta.objects.filter(user=request.user, seccion_id=seccion_id).order_by('?'))
        print(preguntas)
    return preguntas

@login_required
def apropiacionPregunta(request, seccion_id, pregunta_id, numero):
    pregunta = get_object_or_404(Pregunta,pk=pregunta_id,user=request.user)
    pregunta.apropiacion=numero
    pregunta.save()
    print(pregunta.apropiacion)
    return repasoFlashcard(request, seccion_id)

            
