from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    valor = models.IntegerField()
    data = models.DateField(default='2024-01-01')
    hora = models.TimeField(default='00:00:00')