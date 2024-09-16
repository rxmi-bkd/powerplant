from rest_framework import serializers
from .models import Fuels, Powerplant, EnergyLoadRequest
from drf_writable_nested.serializers import WritableNestedModelSerializer


class FuelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuels
        fields = ['gas', 'kerosine', 'co2', 'wind']


class PowerplantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerplant
        fields = ['name', 'type', 'efficiency', 'pmin', 'pmax']


class EnergyLoadRequestSerializer(WritableNestedModelSerializer):
    fuels = FuelsSerializer()
    powerplants = PowerplantSerializer(many=True)

    class Meta:
        model = EnergyLoadRequest
        fields = ['load', 'fuels', 'powerplants']
