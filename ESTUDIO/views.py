from doctest import FAIL_FAST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from ESTUDIO.forms import newPregunta
from ESTUDIO.models import Pregunta
from MAIN.forms import newSeccion

# Create your views here.

@login_required
def crearFlashcard(request, seccion_id):
    if request.method == 'GET':
        return render(request, 'crearFlashcard.html', {
            'form' : newPregunta()
        })
    else:
        Pregunta.objects.create(user = request.user, name = request.POST['name'], respuesta = request.POST['respuesta'], apropiacion = 1, seccion_id = seccion_id)
        return redirect('/materias/')

@login_required
def pregunta_detail(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, user = request.user, pk = pregunta_id)
    return render(request, 'pregunta_detail.html', {
        'pregunta' : pregunta
    })

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
def eliminarPregunta(request, pregunta_id):
    if request.method == 'POST':
        pregunta=get_object_or_404(Pregunta, user=request.user, pk=pregunta_id)
        pregunta.delete()
        return redirect('/materias/')
@login_required
def repasoFlashcard(request, seccion_id):
    if request.method == 'GET':
        preguntas=list(Pregunta.objects.filter(user=request.user, seccion_id=seccion_id).order_by('?'))
        print(preguntas)
        return render(request, 'repaso.html')
