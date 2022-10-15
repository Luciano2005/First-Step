from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('login/' , views.login, name="login"),
    path('register/' , views.register, name="register"),
    path('perfil/' , views.perfil, name="perfil"),
]