from cliente.model.silla import Silla
from rest_framework import serializers

class SillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silla
        fields = '__all__'