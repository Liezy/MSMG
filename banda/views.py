
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Banda
from .forms import BandaForm
from .forms import UserRegistrationForm

def banda_lista(request):
    bandas = Banda.objects.all()
    return render(request, 'banda/banda_lista.html', {'bandas': bandas})

class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'banda/user_register.html'
    success_url = reverse_lazy('banda_lista')

class BandaCriarView(CreateView):
    model = Banda
    form_class = BandaForm
    template_name = 'banda/banda_form.html'
    success_url = reverse_lazy('banda_lista')

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