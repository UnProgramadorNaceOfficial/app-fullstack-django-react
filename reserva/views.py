from rest_framework import viewsets

from reserva.models import Reserva
from reserva.serializer import ReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
