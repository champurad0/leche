from rest_framework import viewsets
from .models import Pump
from .serializers import PumpSerializer


class PumpViewSet(viewsets.ModelViewSet):
    queryset = Pump.objects.all()
    serializer_class = PumpSerializer
