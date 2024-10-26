from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('menuadmin',views.menu_admin, name='menuad'),
    path('estado', EstadoListCreateUpdateView.as_view(), name='menu_estado'),
    path('roles/', RolCRUDView.as_view(), name='rol_view'),  # Lista y CRUD de roles
    path('roles/inactivar/<int:rol_id>/', RolInactivateView.as_view(), name='inactivar_rol'),  # Inactivar rol
    path('menu_permisos',views.permisos,name='menu_permisos'),
    path('permisos/', PermisoCRUDView.as_view(), name='permiso_view'),
    path('roles_permisos',views.sub_roles_permisos, name='roles_permisos'),
]