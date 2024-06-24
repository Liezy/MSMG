
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, View
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Banda
from .forms import BandaForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BandaListaView(LoginRequiredMixin, ListView):
    model = Banda
    template_name = 'banda/banda_lista.html'
    context_object_name = 'bandas'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(num_eventos=Count('eventos'))
        return queryset
    
    def get_queryset(self):
        return Banda.objects.filter(usuario=self.request.user)

class BandaCriarView(CreateView):
    model = Banda
    form_class = BandaForm
    template_name = 'banda/banda_form.html'
    success_url = reverse_lazy('banda_lista')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class BandaUpdateView(UpdateView):
    model = Banda
    form_class = BandaForm
    template_name = 'banda/banda_form.html'
    success_url = reverse_lazy('banda_lista')

class BandaDeleteView(DeleteView):
    model = Banda
    template_name = 'banda/banda_confirm_delete.html'
    success_url = reverse_lazy('banda_lista')

class BandaDetalhesView(DetailView):
    model = Banda
    template_name = 'banda/banda_detalhes.html'
    context_object_name = 'banda'

class ImagemBanda(View):
    def get(self, request, arquivo):
        try:
            banda = get_object_or_404(Banda, imagem='banda/imagens/{}'.format(arquivo))
            if banda.imagem:
                return FileResponse(banda.imagem.open())
            else:
                raise Http404("Imagem não encontrada ou acesso não autorizado!")
        except Banda.DoesNotExist:
            raise Http404("Imagem não encontrada ou acesso não autorizado!")
        except Exception as exception:
            raise exception