from doctest import FAIL_FAST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from ESTUDIO.forms import newPregunta
from ESTUDIO.models import Pregunta
from MAIN.forms import newSeccion

# Create your views here.
def crearFlashcard(request, seccion_id):
    if request.method == 'GET':
        return render(request, 'crearFlashcard.html', {
            'form' : newPregunta()
        })
    else:
        form=newPregunta(request.POST)
        nueva_pregunta=form.save(commit=False)
        nueva_pregunta.user=request.user
        nueva_pregunta.save()
        return redirect('/materias/')