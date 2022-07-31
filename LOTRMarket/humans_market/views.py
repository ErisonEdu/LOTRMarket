from rest_framework import viewsets, permissions
from LOTRMarket.humans_market.models import HumanItem
from .serializers import HumanItemSerializer

class HumanItemAPIViewSet(viewsets.ModelViewSet):
        queryset = HumanItem.objects.all()
        serializer_class = HumanItemSerializer
        permission_classes = [permissions.IsAuthenticated]