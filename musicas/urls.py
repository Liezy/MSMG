from django.urls import path
from .views import MusicaListaView, MusicaDetalhesView, MusicaCriarView

urlpatterns = [
    path('', MusicaListaView.as_view(), name='musica_lista'),
    path('<int:pk>/', MusicaDetalhesView.as_view(), name='musica_detalhes'),
    path('nova/', MusicaCriarView.as_view(), name='musica_criar'),
]
