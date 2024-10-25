from django.shortcuts import render
from core.models import *

# Create your views here.

def navbar (request):
    return render(request, 'prueba.html')

def menu(request):
    return render(request, 'menu.html')

def jugadores(request):
    return render(request, 'jugadores.html')

def listjugadores(request):
    return render(request, 'listjugadores.html')

# def menuinit (request):
#         return render(request, 'menu.html')
