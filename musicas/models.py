from django.db import models
from eventos.models import Evento

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    audio_link = models.URLField(blank=True, null=True)
    letra_link = models.URLField(blank=True, null=True)
    cifra_link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='musicas')

    def __str__(self):
        return self.titulo
