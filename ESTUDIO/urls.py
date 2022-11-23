from django.urls import path
from . import views

urlpatterns=[
    #Flashcard
    path('<int:seccion_id>',views.crearFlashcard,name='crearFlashcard'),
    path('pregunta_detail/<int:pregunta_id>', views.pregunta_detail, name = 'pregunta_detail'),
    path('cambiarPregunta/redireccionando/<int:pregunta_id>', views.redireccionarPregunta, name = 'redireccionarPregunta'),
    path('cambiarPregunta/<int:pregunta_id>', views.cambiarPregunta, name = 'cambiarPregunta'),

    #Pregunta cerrada
    path('crearPreguntaCerrada/<int:seccion>/',views.crearPreguntaCerrada,name='crearPreguntaCerrada'),
    path('crearPreguntaCerrada/<int:seccion>/crearRespuestaCerrada',views.crearRespuestaCerrada,name='crearRespuestaCerrada'),
    path('crearPreguntaCerrada/<int:seccion>/eliminarRespuestaCerrada',views.eliminarRespuestaCerrada,name='eliminarRespuestaCerrada'),
    path('cambiarPreguntaCerrada/<int:pregunta_id>', views.cambiarPreguntaCerrada, name = 'pregunta_cerrada'),
    path('cambiarPreguntaCerrada/<int:pregunta_id>/<int:size>', views.cambiarPreguntaCerrada, name = 'nueva_respuesta_cerrada'),
    path('cambiarPreguntaCerrada/<int:pregunta_id>/<int:eliminar>', views.cambiarPreguntaCerrada, name = 'eliminar_nueva_respuesta_cerrada'),
    path('eliminarPregunta/<int:pregunta_id>', views.eliminarPregunta, name = 'eliminarPregunta'),

    #Repaso
    path('repaso/<int:seccion_id>', views.repasoFlashcard, name = 'repaso'),
    path('repaso/<int:seccion_id>/<int:pregunta_id>/<int:numero>', views.apropiacionPregunta, name='apropiacionPregunta'),

    #Pomodoro
    path('pomodoro', views.pomodoro, name='pomodoro')
]