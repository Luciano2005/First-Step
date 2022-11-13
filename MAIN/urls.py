from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #Login y Register
    path('', views.main, name='main'),
    path('formlogin/' , views.formlogin, name='login'),
    path('register/' , views.register, name='register'),
    path('perfil/' , views.perfil, name='perfil'),
    path('logout/',views.logout2,name='logout'),
    
    #Recuperar contraseña
    path('resetPassword/', auth_views.PasswordResetView.as_view(template_name = 'resetPassword.html'), name = 'reset_password'),
    path('resetPasswordSent/', auth_views.PasswordResetDoneView.as_view(template_name = 'resetPasswordSent.html'), name = 'password_reset_done'),
    path('resetPasswordConfirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "resetPasswordForm.html"), name = 'password_reset_confirm'),
    path('resetPasswordComplete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'resetPasswordComplete.html'), name = 'password_reset_complete'),
    
    #Materias
    path('materias/', views.materias, name = 'materias'),
    path('crearMateria/', views.crearMateria, name = 'crearMateria'),
    path('materia_detail/<int:materia_id>',views.materia_detail, name = 'materia_detail'),
    path('cambiarMateria/<int:materia_id>',views.cambiarMateria, name = 'cambiarMateria'),
    path('eliminarMateria/<int:materia_id>', views.elmimiarMateria, name = 'eliminarMateria'),

    #Archivos
    path('materias/<int:materia_id>/verArchivos', views.verArchivos, name='verArchivos'),
    path('materias/<int:materia_id>/agregarArchivos', views.agregarArchivos, name='agregarArchivos'),
    path('materias/<int:archivo_id>/eliminarArchivo', views.eliminarArchivo, name='eliminarArchivo'),

    #Sección
    path('crearSeccion/<int:materia_id>', views.crearSeccion, name = 'crearSeccion'),
    path('seccion_detail/<int:seccion_id>',views.seccion_detail ,name='seccion_detail'),
    path('cambiarSeccion/<int:seccion_id>',views.cambiarSeccion ,name='cambiarSeccion'),
    path('eliminarSeccion/<int:seccion_id>',views.eliminarSeccion ,name='eliminarSeccion'),

    #Tareas
    path('tareas/', views.mostrarTareas, name='mostrarTareas'),
    path('tareas/<int:tarea_id>', views.tarea_detail, name='tarea_detail'),
    path('tareas/crearTarea',views.crearTarea,name='crearTarea'),
    path('actualizarTarea/<int:tarea_id>', views.actualizarTarea, name='actualizarTarea'),
    path('eliminarTarea/<int:tarea_id>', views.eliminarTarea, name='eliminarTarea'),
    
]