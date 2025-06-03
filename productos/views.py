from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

from django.contrib import messages
from django.urls import reverse

import os
import mercadopago

# Create your views here.

MP_ACCESS_TOKEN = os.getenv('MP_ACCESS_TOKEN')
MP_PUBLIC_KEY = os.getenv('MP_PUBLIC_KEY')

sdk = mercadopago.SDK(MP_ACCESS_TOKEN)

def producto_lista(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def producto_detalle(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    preference = gen_preference_mp(request, prod)
    context = {
        'producto': prod,
        'MP_PUBLIC_KEY': MP_PUBLIC_KEY,
        'preference_id': preference["id"],
    }
    return render(request, 'productos/detalle.html', context)

def producto_agregar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        if nombre and precio:
            Producto.objects.create(nombre=nombre, precio=precio)
            return redirect('producto_lista')
    return render(request, 'productos/agregar.html')

def gen_preference_mp(request, prod):
    preference_data = {
        "items": [{
            "title": f"{prod.nombre}",
            "quantity": 1,
            "unit_price": max(int(prod.precio), 1),
        }],
        "back_urls": {
            "success": request.build_absolute_uri(reverse('payment_success')),
            "failure": request.build_absolute_uri(reverse('payment_failure')),
            "pending": request.build_absolute_uri(reverse('payment_pending'))
        },
        "auto_return":
        "approved",
    }
    preference_response = sdk.preference().create(preference_data)
    return preference_response["response"]

def payment_success(request):
    messages.success(request, '¡Pago realizado con éxito!')
    return redirect('producto_lista')

def payment_failure(request):
    messages.error(request, 'El pago no pudo ser procesado. Por favor, intenta nuevamente.')
    return redirect('producto_lista')

def payment_pending(request):
    messages.warning(request, 'Tu pago está pendiente de confirmación.')
    return redirect('producto_lista')
