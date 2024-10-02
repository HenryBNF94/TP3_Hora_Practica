from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def hola(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())