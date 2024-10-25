from django.shortcuts import render
from core.models import *
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.

# class EstadoListView(ListView):
#     model= Estado
#     template_name = 'estado_list.html'
#     context_object_name = 'estados'