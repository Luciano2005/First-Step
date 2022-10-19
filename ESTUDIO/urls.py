from django.urls import path
from . import views
urlpatterns=[
    path('',views.crearFlashcard,name='crearFlashcard')
]