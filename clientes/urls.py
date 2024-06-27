#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.clientes_registro, name='registro'),
    path('registro_usuario', views.clientes_registro_usuario, name="registro_usuario"),
    path('menu', views.clientes_menu, name='menu'),
    path('home', views.clientes_home, name='home'),
    path('base', views.base, name='base'),
]