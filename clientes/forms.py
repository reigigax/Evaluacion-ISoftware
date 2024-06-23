from django import forms
from .models import Usuario, Empresa

from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ["rut", "nombre", "apellido_paterno", "apellido_materno", "fecha_nacimiento", "id_empresa_asociada", "correo", "telefono", "direccion", "activo"]
        labels = {'rut':'Rut',
                  'nombre':'Nombre',
                  'apellido_paterno':'Apellido Paterno',
                  'apellido_materno':'Apellido Materno',
                  'fecha_nacimiento':'Fecha De Nacimiento',
                  'id_empresa_asociada':'Empresa',
                  'correo':'Correo',
                  'telefono':'Teléfono',
                  'direccion':'Direccion',
                  'activo':'Activo',
                 }