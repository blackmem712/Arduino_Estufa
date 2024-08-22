from django.db import models
from django.utils import timezone

class Estufa(models.Model):
  nome = models.CharField(max_length=50 , null=True, blank=True)
  setor = models.CharField(max_length=20, null=True, blank=True)
  descricao = models.CharField(max_length=100, null=True, blank=True)

def __str__(self) -> str:
    return self.nome

class SensorData(models.Model):
    umidade = models.FloatField()
    temperatura = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Umidade: {self.umidade}%, Temperatura: {self.temperatura}°C"