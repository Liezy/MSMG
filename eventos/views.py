from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Evento
from .forms import EventoForm
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .serializers import EventoSerializer

class EventoListaView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'eventos/evento_lista.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        return Evento.objects.filter(usuario=self.request.user)

class EventoDetalhesView(DetailView):
    model = Evento
    template_name = 'eventos/evento_detalhes.html'
    context_object_name = 'evento'

class EventoCriarView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('evento_lista')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('evento_lista')

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'eventos/evento_confirmacao_delete.html'
    success_url = reverse_lazy('evento_lista')

class EventoListAPIView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    
class EventoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer