from rest_framework import viewsets, permissions
from LOTRMarket.elves_market.models import ElvenItem
from .serializers import ElvenItemSerializer

class ElvenItemAPIViewSet(viewsets.ModelViewSet):
    queryset = ElvenItem.objects.all()
    serializer_class = ElvenItemSerializer
    permission_classes = [permissions.IsAuthenticated]