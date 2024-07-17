from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Usuario, Empresa
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
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            login(request, user)

            form=UserCreationForm()
            context={'mensaje':"Ok, datos grabados...", "form":form}

            return redirect('menu')
    else:
        form = UserCreationForm()
        context = {"form":form}
        return render(request, '../templates/registration/register.html', context)
    
# Pagina Base de estilos o pruebas
def base(request):
    context = {}
    return render(request, 'clientes_base.html', context)



# Paginas de administracion
def administrador_crud(request):
    usuarios = Usuario.objects.all()
    empresa_asociada = Empresa.objects.all()
    cuentas_usuarios = User.objects.all()

    context = {
        'usuarios':usuarios, 
        'empresa_asociada':empresa_asociada,
        'cuentas_usuarios' : cuentas_usuarios
    }
    return render(request, 'administrador/administrador_crud.html',context)



def eliminar_cuenta_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('crud')
    return render(request, 'administrador/eliminar_cuenta.html',{'usuario':usuario})

def modificar_cuenta_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        # Recibir los datos del formulario
        username = request.POST['username']
        email = request.POST['email']
        
        # Modificar el usuario
        usuario.username = username
        usuario.email = email
        usuario.save()
        
        messages.success(request, 'Usuario modificado correctamente.')
        return redirect('crud')  # Por ejemplo, redirigir a la página de detalle del usuario
    
    # Renderizar un template con el formulario de modificación
    return render(request, 'administrador/modificar_cuenta.html', {'usuario': usuario})

def administrador_agregar_cuenta(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()

            form=UserCreationForm()
            context={'mensaje':"Ok, datos grabados...", "form":form}

            return redirect('crud')
    else:
        form = UserCreationForm()
        context = {"form":form}
        return render(request, '../templates/registration/register.html', context)
    


def administrador_registro_usuario(request):
    context={}

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid:
            form.save()

            form=UsuarioForm()

            context={'mensaje':"Ok, datos grabados...", "form":form}
            return redirect('crud')
    else:
        form = UsuarioForm()
        context = {"form":form}
        return render(request, 'clientes/clientes_registro.html', context)
    
def administrador_eliminacion_usaurio(request, user_rut):
    usuario = get_object_or_404(Usuario, rut=user_rut)
    if request.method == 'POST':
        usuario.delete()
        return redirect('crud')
    return render(request, 'administrador/eliminar_usuario.html', {'usuario':usuario})

def administrador_modificacion_usuario(request, user_rut):
    usuario = get_object_or_404(Usuario, rut=user_rut)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('crud')  # Redirige a la página deseada después de la modificación
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'administrador/modificar_usuario.html', {'form': form, 'usuario': usuario})