from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Musica
from .forms import MusicaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .serializers import MusicaSerializer

class MusicaListaView(LoginRequiredMixin, ListView):
    model = Musica
    template_name = 'musicas/musica_lista.html'
    context_object_name = 'musicas'

    def get_queryset(self):
        return Musica.objects.filter(usuario=self.request.user)

class MusicaDetalhesView(DetailView):
    model = Musica
    template_name = 'musicas/musica_detalhes.html'
    context_object_name = 'musica'

class MusicaCriarView(CreateView):
    model = Musica
    form_class = MusicaForm
    template_name = 'musicas/musica_form.html'
    success_url = reverse_lazy('musica_lista')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class MusicaAtualizarView(UpdateView):
    model = Musica
    form_class = MusicaForm
    template_name = 'musicas/musica_form.html'
    success_url = reverse_lazy('musica_lista')

class MusicaDeletarView(DeleteView):
    model = Musica
    template_name = 'musicas/musica_confirm_delete.html'
    success_url = reverse_lazy('musica_lista')

class MusicaListAPIView(generics.ListCreateAPIView):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
    
class MusicaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer