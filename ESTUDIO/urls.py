from django.urls import path
from . import views

urlpatterns=[
    path('<int:seccion_id>',views.crearFlashcard,name='crearFlashcard'),
    path('pregunta_detail/<int:pregunta_id>', views.pregunta_detail, name = 'pregunta_detail'),
    path('cambiarPregunta/<int:pregunta_id>', views.cambiarPregunta, name = 'cambiarPregunta'),
    path('eliminarPregunta/<int:pregunta_id>', views.eliminarPregunta, name = 'eliminarPregunta'),
    path('repaso/<int:seccion_id>', views.repasoFlashcard, name = 'repaso')
]