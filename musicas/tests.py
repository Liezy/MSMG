from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Musica
from musicas.serializers import MusicaSerializer

class MusicaAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.musica = Musica.objects.create(
            titulo='Música Teste',
            audio_link='https://example.com/audio.mp3',
            letra_link='https://example.com/letra.txt',
            cifra_link='https://example.com/cifra.txt',
            video_link='https://example.com/video.mp4',
            usuario=self.user
        )

    def test_lista_musicas(self):
        url = reverse('musica-list')
        response = self.client.get(url)
        musicas = Musica.objects.all()
        serializer = MusicaSerializer(musicas, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_detalhes_musica(self):
        url = reverse('musica-detail', kwargs={'pk': self.musica.pk})
        response = self.client.get(url)
        serializer = MusicaSerializer(self.musica)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
