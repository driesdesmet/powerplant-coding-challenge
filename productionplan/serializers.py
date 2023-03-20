from rest_framework import serializers


class PayLoadSerializer(serializers.Serializer):
    load = serializers.IntegerField(min_value=0)
    fuels = serializers.DictField()
    powerplants = serializers.ListField()
