from django.urls import path
from . import views

urlpatterns = [
    path('',views.menu, name='menu'),
    path('jugadores', views.jugadores, name='jugadores'),
    path('listjugadores', views.listjugadores, name='listjugadores')
]