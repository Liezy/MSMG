from django.urls import path
from .views import MusicaListaView, MusicaDetalhesView, MusicaCriarView, MusicaAtualizarView, MusicaDeletarView, MusicaListAPIView, MusicaDetailAPIView

urlpatterns = [
    path('', MusicaListaView.as_view(), name='musica_lista'),
    path('<int:pk>/', MusicaDetalhesView.as_view(), name='musica_detalhes'),
    path('nova/', MusicaCriarView.as_view(), name='musica_criar'),
    path('<int:pk>/editar/', MusicaAtualizarView.as_view(), name='musica_editar'),
    path('<int:pk>/deletar/', MusicaDeletarView.as_view(), name='musica_deletar'),
    path('api/musicas/', MusicaListAPIView.as_view(), name='musica-list'),
    path('api/musicas/<int:pk>/', MusicaDetailAPIView.as_view(), name='musica-detail'),
]
