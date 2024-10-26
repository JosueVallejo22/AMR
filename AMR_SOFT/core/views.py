from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from core.models import Jugador
from core.forms import JugadorForm


# Create your views here.

def navbar (request):
    return render(request, 'prueba.html')

def menu(request):
    return render(request, 'menu.html')

def jugadores(request):
    return render(request, 'jugadores.html')

def listjugadores(request):
    return render(request, 'listjugadores.html')

# def menuinit (request):
#         return render(request, 'menu.html')

class jugadorListView(ListView):
  template_name = "listjugadores.html"
  context_object_name = 'jugadores'
  model = Jugador

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['listar_url'] = '/listajugador/'
    context['crear_url'] = '/crearjugador/'
    context['query'] = self.request.GET.get("query")
    return context

class jugadorCreateView(CreateView):
    template_name = 'jugadores.html'
    model = Jugador
    form_class = JugadorForm
    success_url = reverse_lazy('listajugador')


    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['boton1'] = "Guardar Registro" 
      context['boton2'] = "Cancelar registro" 
      context['listar_url'] = reverse_lazy('listajugador')
      context['action_save'] = reverse_lazy('crearjugador') 
    #   context['mensaje'] = 'Creado'
      return context
    
    def form_valid(self, form):
       form.instance.created_by = self.request.user
       return super().form_valid(form)