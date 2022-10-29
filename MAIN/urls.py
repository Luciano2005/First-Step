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
    path('eliminarMateria/<int:materia_id>', views.elmimiarMateria, name = 'eliminarMateria'),
    path('crearSeccion/<int:materia_id>', views.crearSeccion, name = 'crearSeccion'),
    path('seccion_detail/<int:seccion_id>',views.seccion_detail ,name='seccion_detail'),
    path('cambiarSeccion/<int:seccion_id>',views.cambiarSeccion ,name='cambiarSeccion'),
    path('eliminarSeccion/<int:seccion_id>',views.eliminarSeccion ,name='eliminarSeccion'),

    #Vista de Tareas
    path('tareas/', views.mostrarTareas, name='mostrarTareas'),
    path('tareas/<int:tarea_id>', views.tarea_detail, name='tarea_detail'),
    path('tareas/crearTarea',views.crearTarea,name='crearTarea')

]