from django.urls import path
from .views import BandaListaView, BandaCriarView, BandaUpdateView, BandaDeleteView, BandaDetalhesView, ImagemBanda

urlpatterns = [
    path('', BandaListaView.as_view(), name='banda_lista'),
    path('criar/', BandaCriarView.as_view(), name='banda_criar'),
    path('editar/<int:pk>/', BandaUpdateView.as_view(), name='banda_editar'),
    path('deletar/<int:pk>/', BandaDeleteView.as_view(), name='banda_deletar'),
    path('<int:pk>/', BandaDetalhesView.as_view(), name='banda_detalhes'),
    path('imagens/<str:arquivo>/', ImagemBanda.as_view(), name='imagem-banda'),
]