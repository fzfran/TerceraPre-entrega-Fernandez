from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from perifericos.models import Periferico
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ListadoPerifericos(ListView):
    model = Periferico
    context_object_name = 'lista_de_perifericos'
    template_name = 'perifericos.html'
    
class PerifericoModelCreateView(LoginRequiredMixin, CreateView):
    model = Periferico
    template_name = "crear_perifericos.html"
    fields = ['marca', 'modelo', 'fecha_de_creacion']
    success_url = reverse_lazy('perifericos')

class ActualizarPeriferico(LoginRequiredMixin, UpdateView):
    model = Periferico
    template_name = "actualizar_perifericos.html"
    fields = ['marca', 'modelo', 'fecha_de_creacion']
    success_url = reverse_lazy('perifericos')
    
class BorrarPeriferico(LoginRequiredMixin, DeleteView):
    model = Periferico
    template_name = "eliminar_perifericos.html"
    success_url = reverse_lazy('perifericos')
    
class DetallePeriferico(DetailView):
    model = Periferico
    template_name = "detalle_perifericos.html"
