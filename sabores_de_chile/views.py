from django.shortcuts import render
from .models import Producto

def inicio(request):
    return render(request, 'templateApp/inicio.html')

def menu(request):
    productos = Producto.objects.all()  # Trae todos los productos de la base
    return render(request, 'templateApp/menu.html', {'productos': productos})

def carrito(request):
    return render(request, 'templateApp/carrito.html')
