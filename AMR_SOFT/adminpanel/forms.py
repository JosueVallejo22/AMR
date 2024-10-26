from django import forms
from .models import *

#FORMULARIOS PARA EL PANEL ADMINISTRATIVO
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['estado', 'descripcion']
    
    def limpiar_estado(self):
        estado = self.cleaned_data.get('estado').upper()
        if Estado.objects.filter(estado_iexact=estado).exists():
            raise forms.ValidationError("El Estado ya existe. Ingrese uno diferente.")
        return estado

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['rol', 'estado']

class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = ['permiso', 'descripcion', 'estado']   