from django.urls import path
from .views import EventoListaView, EventoDetalhesView, EventoCriarView, EventoUpdateView, EventoDeleteView, EventoListAPIView, EventoDetailAPIView

urlpatterns = [
    path('', EventoListaView.as_view(), name='evento_lista'),
    path('<int:pk>/', EventoDetalhesView.as_view(), name='evento_detalhes'),
    path('novo/', EventoCriarView.as_view(), name='evento_criar'),
    path('<int:pk>/edit/', EventoUpdateView.as_view(), name='evento_edit'),
    path('<int:pk>/delete/', EventoDeleteView.as_view(), name='evento_delete'),
    path('api/eventos/', EventoListAPIView.as_view(), name='evento-list'),
    path('api/eventos/<int:pk>/', EventoDetailAPIView.as_view(), name='evento-detail'),
]
