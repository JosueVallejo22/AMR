from django.urls import path, include
from . import views

urlpatterns = [
    path('menuadmin',views.menu_admin, name='menuad'),
    path('estado',views.estados,name='estados'),
    path('roles',views.roles,name='roles'),
    path('menu_permisos',views.permisos,name='menu_permisos'),
    path('permisos',views.subpermisos,name='permisos'),
    path('roles_permisos',views.sub_roles_permisos, name='roles_permisos'),
]