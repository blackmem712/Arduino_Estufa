from django.db import models

class Estufa(models.Model):
  nome = models.CharField(max_length=50 , null=True, blank=True)
  temperatura = models.CharField(max_length=20, null=True, blank=True)
  umidade = models.CharField(max_length=20, null=True, blank=True)
  setor = models.CharField(max_length=20, null=True, blank=True)
  descricao = models.CharField(max_length=100, null=True, blank=True)

def __str__(self) -> str:
    return self.nome
