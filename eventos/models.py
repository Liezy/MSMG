# eventos/models.py
from django.db import models
from banda.models import Banda
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    local = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='eventos')
    musicas = models.ManyToManyField('musicas.Musica', blank=True, related_name='eventos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
