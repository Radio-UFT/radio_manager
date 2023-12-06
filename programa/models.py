from django.db import models
from datetime import datetime

class Programa(models.Model):
  nome = models.CharField(max_length=100)
  descricao = models.TextField(max_length=200)
  horario = models.TimeField()
  foto = models.ImageField(blank=True, null=False, upload_to='programa/fotos')

  def __str__(self):
    return self.nome