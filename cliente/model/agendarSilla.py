from django.db import models
from django.conf import settings
from .silla import Silla

class AgendarSilla(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    silla = models.ForeignKey(Silla, on_delete=models.CASCADE)
    fecha = models.DateField()