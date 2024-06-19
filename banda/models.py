from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Banda(models.Model):
    nome = models.CharField(max_length=100)
    membros = models.ManyToManyField(User, related_name='bandas')

    def __str__(self):
        return self.nome
    
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    local = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='banda_eventos') 

    def __str__(self):
        return self.titulo