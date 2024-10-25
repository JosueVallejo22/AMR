from django.urls import path, include
from . import views

urlpatterns = [
    path('menuadmin',views.menu_admin, name='menuad'),
    path('estado',views.estados,name='estados'),
    path('roles',views.roles,name='roles'),
    path('permisos',views.permisos,name='permisos'),
]