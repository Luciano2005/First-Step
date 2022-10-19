from django.urls import path
from . import views
urlpatterns=[
    path('<int:seccion_id>',views.crearFlashcard,name='crearFlashcard')
]