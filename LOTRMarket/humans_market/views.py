from rest_framework import viewsets, permissions
from LOTRMarket.humans_market.models import HumanItem, HumanWeapon
from .serializers import HumanItemSerializer, HumanWeaponSerializer

class HumanItemAPIViewSet(viewsets.ModelViewSet):
        queryset = HumanItem.objects.all()
        serializer_class = HumanItemSerializer
        permission_classes = [permissions.IsAuthenticated]

class HumanWeaponAPIViewSet(viewsets.ModelViewSet):
        queryset = HumanWeapon.objects.all()
        serializer_class = HumanWeaponSerializer
        permission_classes = [permissions.IsAuthenticated]