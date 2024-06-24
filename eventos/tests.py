from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from banda.models import Banda
from .models import Evento
from eventos.serializers import EventoSerializer

class EventoAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.banda = Banda.objects.create(nome='Banda Teste', usuario=self.user)
        self.evento = Evento.objects.create(
            titulo='Evento Teste',
            descricao='Descrição do Evento',
            data='2024-07-01',
            local='Local do Evento',
            banda=self.banda,
            usuario=self.user
        )

    def test_lista_eventos(self):
        url = reverse('evento-list')
        response = self.client.get(url)
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_detalhes_evento(self):
        url = reverse('evento-detail', kwargs={'pk': self.evento.pk})
        response = self.client.get(url)
        serializer = EventoSerializer(self.evento)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
