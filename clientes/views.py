from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UsuarioForm, UserCreationForm

# Create your views here.

@login_required
def clientes_menu(request):
    #request.session[""]
    context={}
    return render(request, 'clientes/clientes_menu.html', context)

def clientes_home(request):
    #request.session[""]
    context={}
    return render(request, 'clientes/clientes_home.html', context)

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
    
# base de estilos o pruebas
def base(request):
    context = {}
    return render(request, 'clientes_base.html', context) 