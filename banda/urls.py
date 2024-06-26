from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import BandaListaView, BandaCriarView, BandaUpdateView, BandaDeleteView, BandaDetalhesView, ImagemBanda, BandaListAPIView, BandaDetailAPIView

urlpatterns = [
    path('', BandaListaView.as_view(), name='banda_lista'),
    path('criar/', BandaCriarView.as_view(), name='banda_criar'),
    path('editar/<int:pk>/', BandaUpdateView.as_view(), name='banda_editar'),
    path('deletar/<int:pk>/', BandaDeleteView.as_view(), name='banda_deletar'),
    path('<int:pk>/', BandaDetalhesView.as_view(), name='banda_detalhes'),
    path('imagens/<str:arquivo>/', ImagemBanda.as_view(), name='imagem-banda'),
    path('api/bandas/', BandaListAPIView.as_view(), name='api-bandas-list'),
    path('api/bandas/<int:pk>/', BandaDetailAPIView.as_view(), name='banda-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)