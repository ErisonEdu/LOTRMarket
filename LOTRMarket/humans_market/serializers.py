from rest_framework import serializers
from LOTRMarket.humans_market.models import HumanItem, HumanWeapon

class HumanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanItem
        fields = ("name", "description", "value")

class HumanWeaponSerializer(serializers.ModelSerializer):
    class Meta: 
        model = HumanWeapon
        fields = ("name", "categories", "description", "value")