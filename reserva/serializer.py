from rest_framework import serializers
from .models import Reserva
from cliente.models import Cliente
from establecimiento.models import Establecimiento
from datetime import timedelta

class ReservaSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    establecimiento = serializers.PrimaryKeyRelatedField(queryset=Establecimiento.objects.all())

    class Meta:
        model = Reserva
        fields = ['id', 'fecha', 'descripcion', 'valor', 'email', 'cliente', 'establecimiento']

    def validate(self, data):
        fecha = data['fecha']
        establecimiento = data['establecimiento']
        nueva_inicio = fecha
        nueva_fin = fecha + timedelta(hours=3)

        # Verificar si existe alguna reserva en conflicto con ese rango de 3 horas
        conflicto = Reserva.objects.filter(
            establecimiento=establecimiento,
            fecha__lt=nueva_fin,
            fecha__gt=nueva_inicio - timedelta(hours=3)
        ).exclude(id=self.instance.id if self.instance else None).order_by('fecha').first()

        if conflicto:
            fin_conflicto = conflicto.fecha + timedelta(hours=3)
            tiempo_restante = fin_conflicto - nueva_inicio
            if tiempo_restante.total_seconds() > 0:
                horas = tiempo_restante.seconds // 3600
                minutos = (tiempo_restante.seconds % 3600) // 60
                raise serializers.ValidationError({
                    "Response": f"El establecimiento no está disponible. Intenta reservar en {horas}h {minutos}min (libre a partir de {fin_conflicto.strftime('%Y-%m-%d %H:%M')})."
                })

        return data
