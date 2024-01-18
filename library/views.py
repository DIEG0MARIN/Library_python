from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request,'libros/index.html', {'libros': libros})

def crear_libro(request):
    formulario = LibroForm(request.POST or None)
    return render(request, 'libros/crear.html')

def editar(request):
    return render(request, 'libros/editar.html')

#CONTINUAR EN MINUTO 1:50:00 RELIZAR EN GITHUB RESTO DE CODIFICACION
#Y LUEGO TRAER DETALLES CON UN PULL