from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from adminpanel.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.views import *
from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.contrib import messages

# Create your views here.

def menu_admin(request):
    return render(request, 'menuadmin.html')

def roles(request):
    return render(request, 'menu_roles.html')

def permisos(request):
    return render(request, 'menu_permisos.html')

def subpermisos(request):
    return render(request, 'permisos.html')

def sub_roles_permisos (request):
    return render(request, 'roles-permisos.html')


#Vista para el modelo ESTADO


from django.shortcuts import redirect, get_object_or_404

class EstadoListCreateUpdateView(ListView, FormView):
    model = Estado
    template_name = 'menu_estado.html'
    context_object_name = 'estados'
    form_class = EstadoForm
    success_url = reverse_lazy('menu_estado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estado_id = self.request.GET.get('id')
        if estado_id:
            context['form'] = EstadoForm(instance=get_object_or_404(Estado, id=estado_id))
        else:
            context['form'] = EstadoForm()  # Formulario vacío para creación
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        estado_id = request.POST.get('id')

        if action == 'delete' and estado_id:
            estado = get_object_or_404(Estado, id=estado_id)
            try:
                estado.delete()
                return redirect(self.success_url)
            except ProtectedError:
                # Manejar el error si el estado está relacionado con otros modelos
                messages.error(request, "No se puede eliminar el estado porque está referenciado por otros elementos.")
                return redirect(self.success_url)

        if estado_id:
            # Actualización del estado
            estado = get_object_or_404(Estado, id=estado_id)
            form = EstadoForm(request.POST, instance=estado)
        else:
            # Creación de un nuevo estado
            form = EstadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form))

 # Vista para el modulo de ROLES

class RolCRUDView(ListView, FormView):
    model = Rol
    template_name = 'menu_roles.html'
    context_object_name = 'roles'
    form_class = RolForm
    success_url = reverse_lazy('rol_view')

    def get_queryset(self):
        # Filtrar solo roles activos
        return Rol.objects.filter(estado__id=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = Estado.objects.all()
        
        # Cargar el rol a editar si se pasa un ID
        rol_id = self.request.GET.get('id')
        if rol_id:
            context['rol_edit'] = get_object_or_404(Rol, id=rol_id)
        
        return context

    def form_valid(self, form):
        rol_id = self.request.POST.get('id')
        if rol_id:  # Si existe un ID, se está actualizando
            rol = get_object_or_404(Rol, id=rol_id)
            form = RolForm(self.request.POST, instance=rol)
        else:  # Crear un nuevo rol
            form = RolForm(self.request.POST)

        if form.is_valid():
            form.save()
            return super().form_valid(form)
        
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))



class RolInactivateView(View):
    def post(self, request, rol_id):
        rol = get_object_or_404(Rol, id=rol_id)
        estado_inactivo = Estado.objects.get(id=2)  # Asumiendo que '2' es el id para 'Inactivo'
        
        # Cambiar el estado del rol a inactivo
        rol.estado = estado_inactivo
        rol.save()
        return redirect('rol_view')


#Vistas para el modulo de permisos
class PermisoCRUDView(ListView, FormView):
    model = Permiso
    template_name = 'permisos.html'
    context_object_name = 'permisos'
    form_class = PermisoForm
    success_url = reverse_lazy('permiso_view')

    def get_queryset(self):
        # Filtrar solo permisos activos
        return Permiso.objects.filter(estado__id=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = Estado.objects.all()

        # Cargar el permiso a editar si se pasa un ID
        permiso_id = self.request.GET.get('id')
        if permiso_id:
            context['permiso_edit'] = get_object_or_404(Permiso, id=permiso_id)

        return context

    def form_valid(self, form):
        permiso_id = self.request.POST.get('id')
        print("Datos recibidos:", self.request.POST)  # Debug: verificar datos del formulario

        if permiso_id:  # Si existe un ID, se está actualizando
            permiso = get_object_or_404(Permiso, id=permiso_id)
            permiso.permiso = form.cleaned_data['permiso']
            permiso.descripcion = form.cleaned_data['descripcion']
            permiso.estado = form.cleaned_data['estado']
            permiso.save()
            print("Permiso actualizado:", permiso)  # Debug: verificar datos guardados
        else:  # Crear un nuevo permiso
            permiso = form.save()
            print("Nuevo permiso creado:", permiso)  # Debug: verificar nuevo registro creado

        return super().form_valid(form)


    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))