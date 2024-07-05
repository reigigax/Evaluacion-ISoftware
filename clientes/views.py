from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UsuarioForm, UserCreationForm

# Create your views here.

# Pagina de Menú - Login* 
@login_required
def clientes_menu(request):
    context={}
    return render(request, 'clientes/clientes_menu.html', context)

# Pagina Principal
def clientes_home(request):
    context={}
    return render(request, 'clientes_home.html', context)

# Pagina de Registro de Datos
def clientes_registro(request):
    context={}

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid:
            form.save()

            form=UsuarioForm()

            context={'mensaje':"Ok, datos grabados...", "form":form}
            return redirect('registro_usuario')
    else:
        form = UsuarioForm()
        context = {"form":form}
        return render(request, 'clientes/clientes_registro.html', context)

# Pagina de Registro de Cuentas de Usuario
def clientes_registro_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()

            form=UserCreationForm()

            context={'mensaje':"Ok, datos grabados...", "form":form}
            return redirect('login')

    else:
        form = UserCreationForm()
        context = {"form":form}
        return render(request, '../templates/registration/register.html', context)
    
# Pagina Base de estilos o pruebas
def base(request):
    context = {}
    return render(request, 'clientes_base.html', context) 