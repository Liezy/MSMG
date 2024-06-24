from django.views.generic import View, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .forms import UserRegistrationForm
from django.urls import reverse_lazy

class Login(View):
    """
    Class Based View para autenticação de usuários.
    """

    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            #return HttpResponse('Usuário já está autenticado!')
            return redirect("/bandas")
        else:
            return render(request, 'autenticacao.html', contexto)
    
    def post(self, request):
        
        # obtém as credenciais de autenticação do formulário
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        # verifica as credenciais de auteticação fornecidas
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:

            #verifica se o usuario está ativo no sistema
            if user.is_active:
                login(request, user)
                #return HttpResponse('usuário autenticado com sucesso!')
                return redirect("/bandas")

            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo.'})
                                                        
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou Senha incorretos.'})
    
class Logout(View):
    """
    Class Based View para realizar logout de usuários.
    """

    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
    
class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('index')