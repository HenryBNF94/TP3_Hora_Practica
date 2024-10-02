from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader
from .models import Producto

# Create your views here.

def hola(request):
    template = loader.get_template(inicio.html)
    return HttpResponse(template.render())

def productos(request):
    productos = Producto.objects.all().values()
    template = loader.get_template('productos.html')
    context = {
        'productos' : productos,
    }
    return HttpResponse(template.render(context, request))