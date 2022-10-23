from django.urls import path
from . import views

urlpatterns=[
    path('<int:seccion_id>',views.crearFlashcard,name='crearFlashcard'),
    path('<int:seccion>/',views.crearRespuestaCerrada,name='crearRespuestaCerrada'),
    path('<int:seccion>/eliminarFlashcard',views.eliminarRespuestaCerrada,name='eliminarRespuestaCerrada'),
    path('pregunta_detail/<int:pregunta_id>', views.pregunta_detail, name = 'pregunta_detail'),
    path('cambiarPregunta/redireccionando/<int:pregunta_id>', views.redireccionarPregunta, name = 'redireccionarPregunta'),
    path('cambiarPregunta/<int:pregunta_id>', views.cambiarPregunta, name = 'cambiarPregunta'),
    path('cambiarPreguntaCerrada/<int:pregunta_id>', views.cambiarPreguntaCerrada, name = 'pregunta_cerrada'),
    path('eliminarPregunta/<int:pregunta_id>', views.eliminarPregunta, name = 'eliminarPregunta'),
    path('repaso/<int:seccion_id>', views.repasoFlashcard, name = 'repaso'),
    path('repaso/<int:seccion_id>/<int:pregunta_id>/<int:numero>', views.apropiacionPregunta, name='apropiacionPregunta')
]