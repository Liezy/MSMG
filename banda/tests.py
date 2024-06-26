from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Banda

class BandaAPITestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.banda = Banda.objects.create(nome='Banda Teste', usuario=self.user)
        self.list_url = '/bandas/api/bandas/'
        self.detail_url = f'/bandas/api/bandas/{self.banda.pk}/'  # Usando o ID da banda criada
    
    def test_listagem_bandas(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Verifica se há exatamente uma banda na resposta
    
    def test_detalhes_banda(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Banda Teste')
        self.assertEqual(response.data['usuario']['id'], self.user.id) # Verifica o ID do usuário criador da banda