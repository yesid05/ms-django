from cliente.model.ruta import Ruta
from rest_framework import serializers

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'