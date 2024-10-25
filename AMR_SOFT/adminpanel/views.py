from django.shortcuts import render
from adminpanel.models import *
# Create your views here.

def menu_admin(request):
    return render(request, 'menuadmin.html')

def estados(request):
    return render(request, 'menu_estado.html')

def roles(request):
    return render(request, 'menu_roles.html')
def permisos(request):
    return render(request, 'menu_permisos.html')