from django.urls import path
from .views import banda_lista, BandaCriarView, BandaUpdateView, BandaDeleteView, UserRegistrationView, BandaDetalhesView

urlpatterns = [
    path('', banda_lista, name='banda_lista'),
    path('criar/', BandaCriarView.as_view(), name='banda_criar'),
    path('editar/<int:pk>/', BandaUpdateView.as_view(), name='banda_editar'),
    path('deletar/<int:pk>/', BandaDeleteView.as_view(), name='banda_deletar'),
    path('registrar/', UserRegistrationView.as_view(), name='user_register'),
    path('<int:pk>/', BandaDetalhesView.as_view(), name='banda_detalhes'),
]
