from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('formlogin/' , views.formlogin, name="login"),
    path('register/' , views.register, name="register"),
    path('perfil/' , views.perfil, name="perfil"),
    path('logout/',views.logout2,name='logout'),
    path('materias/', views.materias, name = 'materias'),
    path('crearMateria/', views.crearMateria, name = 'crearMateria'),
    path('materia_detail/<int:materia_id>',views.materia_detail, name = 'materia_detail'),
    path('cambiarMateria/<int:materia_id>',views.cambiarMateria, name = 'cambiarMateria'),
    path('flashcard/',views.flashcard,name='flashcard')
]