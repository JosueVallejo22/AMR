from django import forms
from django.forms import ModelForm
from django.forms import ValidationError

from core.models import *
class JugadorForm(ModelForm):

  class Meta:
    model = Jugador
    fields = ['nombre','apellido','pais','puesto','fecha_nac','altura','peso','pierna_habil','foto']
    widgets = {
      'nombre': forms.TextInput(attrs={'placeholder':'Ingrese el nombre', 'required': False}),
      'apellido': forms.TextInput(attrs={ 'placeholder': 'Ingrese las Pulgadas', 'required': False}),
      'pais': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca', 'required': False}),
      'fecha_nac': forms.DateInput(attrs={ 'placeholder': 'Ingrese la Marca', 'required': False}),
      'puesto': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca', 'required': False}),
      'pierna_habil': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca', 'required': False}),
      'altura': forms.NumberInput(attrs={ 'required': False}),
      'peso': forms.NumberInput(attrs={ 'required': False}),
      'imagen': forms.FileInput(attrs={ 'required': False}),
      

    }