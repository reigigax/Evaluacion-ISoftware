#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.clientes_registro, name='registro'),
    path('registro_usuario', views.clientes_registro_usuario, name="registro_usuario"),
    path('menu', views.clientes_menu, name='menu'),
    path('home', views.clientes_home, name='home'),
    path('base', views.base, name='base'),

    # Path's de Administrador  
    # Paginas de Administracion de Cuenta
    path('crud', views.administrador_crud, name='crud'),
    path('eliminar_cuenta_usuario/<int:user_id>/', views.eliminar_cuenta_usuario, name='eliminar_cuenta_usuario'),
    path('modificar_cuenta_usuario/<int:user_id>/', views.modificar_cuenta_usuario, name='modificar_cuenta_usuario'),
    path('administrador_agregar_cuenta', views.administrador_agregar_cuenta, name='administrador_agregar_cuenta'),

    # Pagina de Administracion de Usuario
    path('administrador_registro_usuario', views.administrador_registro_usuario, name='administrador_registro_usuario'),
    path('administrador_modificacion_usuario/<str:user_rut>/', views.administrador_modificacion_usuario, name='administrador_modificacion_usuario'),
    path('administrador_eliminacion_usaurio/<str:user_rut>/', views.administrador_eliminacion_usaurio, name='administrador_eliminacion_usaurio'),
]