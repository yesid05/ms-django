from cliente.model.agendarSilla import AgendarSilla
from rest_framework import serializers

class AgendarSillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendarSilla
        fields = '__all__'