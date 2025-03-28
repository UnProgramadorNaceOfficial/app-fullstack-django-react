from rest_framework import serializers
from .models import Establecimiento

class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establecimiento
        fields = ['id', 'nombre', 'tipo', 'direccion', 'ciudad', 'telefono']