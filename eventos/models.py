from django.db import models
from banda.models import Banda

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    local = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return self.titulo
