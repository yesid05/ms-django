from rest_framework import viewsets
from cliente.model.silla import Silla
from cliente.serializer.sillaSerializer import SillaSerializer

class SillaView(viewsets.ModelViewSet):
    serializer_class = SillaSerializer
    queryset = Silla.objects.all()