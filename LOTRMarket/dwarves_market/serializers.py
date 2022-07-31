from rest_framework import serializers
from LOTRMarket.dwarves_market.models import DwarvenItem

class DwarvenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DwarvenItem
        fields = ('name', 'description', 'value')