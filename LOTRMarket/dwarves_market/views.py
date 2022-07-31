from itertools import permutations
from rest_framework import viewsets, permissions
from LOTRMarket.dwarves_market.models import DwarvenItem
from .serializers import DwarvenItemSerializer

class DwarvenItemAPIViewSet(viewsets.ModelViewSet):
        queryset = DwarvenItem.objects.all()
        serializer_class = DwarvenItemSerializer
        permission_classes = [permissions.IsAuthenticated]