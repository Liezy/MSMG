from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Banda(models.Model):
    nome = models.CharField(max_length=100)
    membros = models.ManyToManyField(User, related_name='bandas')

    def __str__(self):
        return self.nome