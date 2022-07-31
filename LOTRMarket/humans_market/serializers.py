from rest_framework import serializers
from LOTRMarket.humans_market.models import HumanItem

class HumanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanItem
        fields = ("name", "description", "value")