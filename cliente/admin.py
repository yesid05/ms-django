from django.contrib import admin
from .model.agendarSilla import AgendarSilla
from .model.ruta import Ruta
from .model.silla import Silla

# Register your models here.
admin.site.register(AgendarSilla)
admin.site.register(Ruta)
admin.site.register(Silla)