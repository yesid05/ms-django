from cliente.model.agendarSilla import AgendarSilla
from rest_framework import serializers

class AgendarSillaSerializer(serializers.ModelSerializer):
    
    silla = serializers.SlugRelatedField(
        read_only=True,
        slug_field='nombre'
    )
    
    usuario = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    
    ruta = serializers.SlugRelatedField(
        read_only=True,
        slug_field='descripcion'
    )
    
    class Meta:
        model = AgendarSilla
        fields = '__all__'