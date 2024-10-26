from django import forms
from django.forms import ModelForm
from django.forms import ValidationError

from core.models import Jugador
class JugadorForm(ModelForm):
  
  peso = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'required': False})
  )
  class Meta:
    model = Jugador
    fields = ['nombre','apellido','pais','puesto','fecha_nac','altura','peso','pierna_habil','foto','estado']
    widgets = {
      'nombre': forms.TextInput(attrs={'placeholder':'Ingrese el nombre', 'required': False}),
      'apellido': forms.TextInput(attrs={ 'placeholder': 'Ingrese las Pulgadas', 'required': False}),
      'pais': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca', 'required': False}),
      'fecha_nac': forms.DateInput(attrs={ 'placeholder': 'Ingrese la fecha (YYYY-MM-DD)', 'required': False, 'type': 'date'}),
      'puesto': forms.Select(attrs={ 'placeholder': '', 'required': False}),
      'pierna_habil': forms.Select(choices=[
                ('der', 'Der'),
                ('izq', 'Izq'),
                ('amb', 'Ambas'),
            ]),
      'altura': forms.NumberInput(attrs={ 'required': False}),
      'imagen': forms.FileInput(attrs={ 'required': False}),
      'estado': forms.Select(attrs={ 'placeholder': '', 'required': False}),
    }

    # def clean_costo(self):
    # object = self.cleaned_data.get('costo')
    # if object <= 0:
    #   raise forms.ValidationError("El precio debe ser mayor que {}.".format(object))
    # return object