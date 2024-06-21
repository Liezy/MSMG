from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Musica
from .forms import MusicaForm
from django.urls import reverse_lazy

class MusicaListaView(ListView):
    model = Musica
    template_name = 'musicas/musica_lista.html'
    context_object_name = 'musicas'

class MusicaDetalhesView(DetailView):
    model = Musica
    template_name = 'musicas/musica_detalhes.html'
    context_object_name = 'musica'

class MusicaCriarView(CreateView):
    model = Musica
    form_class = MusicaForm
    template_name = 'musicas/musica_form.html'
    success_url = reverse_lazy('musica_lista')

class MusicaDeleteView(DeleteView):
    model = Musica
    template_name = 'musicas/musica_confirm_delete.html'
    success_url = reverse_lazy('musica_lista')