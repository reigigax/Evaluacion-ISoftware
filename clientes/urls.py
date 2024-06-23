#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.clientes_login, name='login'),
    path('registro', views.clientes_registro, name='registro')
]