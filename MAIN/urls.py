from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('formlogin/' , views.formlogin, name="login"),
    path('register/' , views.register, name="register"),
    path('perfil/' , views.perfil, name="perfil"),
    path('logout/',views.logout2,name='logout'),
    path('flashcard/',views.flashcard,name='flashcard')
]