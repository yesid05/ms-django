from django.db import models

class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True,max_length=100)
    tiempo = models.TimeField()