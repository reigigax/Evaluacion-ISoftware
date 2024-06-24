from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UsuarioForm

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
            return render(request, 'clientes/clientes_registro.html', context)
    else:
        form = UsuarioForm()
        context = {"form":form}
        return render(request, 'clientes/clientes_registro.html', context)