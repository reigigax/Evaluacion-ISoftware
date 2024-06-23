#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.clientes_registro, name='registro'),
    path('menu', views.clientes_menu, name='menu'),
    path('home', views.clientes_home, name='home'),
]