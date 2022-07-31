from rest_framework import serializers
from LOTRMarket.elves_market.models import ElvenItem

class ElvenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElvenItem
        fields = ('name', 'description', 'value')