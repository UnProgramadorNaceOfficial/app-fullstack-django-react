from rest_framework import serializers
from .models import Reserva
from cliente.serializer import ClienteSerializer
from establecimiento.serializer import EstablecimientoSerializer

class ReservaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    establecimiento = EstablecimientoSerializer(read_only=True)

    class Meta:
        model = Reserva
        fields = ['id', 'fecha', 'descripcion', 'valor', 'cliente', 'establecimiento']