from django.db import models
from eventos.models import Evento
from django.contrib.auth.models import User

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    audio_link = models.URLField(blank=True, null=True)
    letra_link = models.URLField(blank=True, null=True)
    cifra_link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
