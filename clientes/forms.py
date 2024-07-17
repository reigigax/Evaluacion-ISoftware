from django import forms
from .models import Usuario
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User

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
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'id_empresa_asociada': forms.Select(attrs={'class': 'form-select'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        
class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("Las contraseñas ingresadas no coinciden"),
    }
    password1 = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_("Confirmacion de Contraseña"),
        widget=forms.PasswordInput,
        help_text=_("Repite la Contraseña Anteriormente Ingresada.")
    )

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
