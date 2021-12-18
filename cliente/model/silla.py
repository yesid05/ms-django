from django.db import models

class Silla(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True,max_length=50)
    estado = models.BooleanField(default=False)