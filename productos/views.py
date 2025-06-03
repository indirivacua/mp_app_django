from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

# Create your views here.

def producto_lista(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def producto_detalle(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': prod})

def producto_agregar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        if nombre and precio:
            Producto.objects.create(nombre=nombre, precio=precio)
            return redirect('producto_lista')
    return render(request, 'productos/agregar.html')
