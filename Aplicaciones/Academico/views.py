from django.shortcuts import render, redirect
from .models import usuarios
from django.contrib import messages

# Create your views here.


def home(request):
    usuariosListados = usuarios.objects.all()
    messages.success(request, 'Usuarios listados!')
    return render(request, "gestionusuarios.html", {"usuarios": usuariosListados})


def registrarUsuario(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    mail = request.POST['txtmail']

    usuarios = usuarios.objects.create(
        codigo=codigo, nombre=nombre, mail=mail)
    messages.success(request, 'Usuario registrado!')
    return redirect('/')


def edicionUsuario(request, codigo):
    usuarios = usuarios.objects.get(codigo=codigo)
    return render(request, "edicionUsuarios.html", {"usuarios": usuarios})


def editarUsuario(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    mail = request.POST['numCreditos']

    usuarios = usuarios.objects.get(codigo=codigo)
    usuarios.nombre = nombre
    usuarios.mail = mail
    usuarios.save()

    messages.success(request, '¡Usuario actualizado!')

    return redirect('/')


def eliminarUsuario(request, codigo):
    usuarios = usuarios.objects.get(codigo=codigo)
    usuarios.delete()

    messages.success(request, '¡Usuario eliminado!')

    return redirect('/')

# Create your views here.
