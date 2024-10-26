from django.urls import path
from django.conf.urls.static import static
from AMR_SOFT import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views 
from core.views import jugadorListView,jugadorCreateView


urlpatterns = [
    path('',views.menu, name='menu'),
    path('jugadores', views.jugadores, name='jugadores'),
    # path('listjugadores', views.listjugadores, name='listjugadores'),
    path('listajugador/', jugadorListView.as_view(),name='listajugador'),
    path('crearjugador/', jugadorCreateView.as_view(),name='crearjugador'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)