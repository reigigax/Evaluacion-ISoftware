from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Usuario, Empresa

from .forms import UsuarioForm

# Create your views here.

def clientes_login(request):
    context={}
    return render(request, 'clientes/clientes_login.html', context)

def clientes_registro(request):
    context={}

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid:
            form.save()

            form=UsuarioForm()

            context={'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, 'clientes/clientes_registro.html', context)
    else:
        form = UsuarioForm()
        context = {"form":form}
        return render(request, 'clientes/clientes_registro.html', context)