from rest_framework import serializers


class FuelsSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        # We need to declare these field inside __init__, and not as
        # a property of this serializer, because they are not valid
        # python property names.
        super().__init__(*args, **kwargs)
        self.fields['gas(euro/MWh)'] = serializers.DecimalField(
            min_value=0,
            max_digits=20,
            decimal_places=2,
            )
        self.fields['kerosine(euro/MWh)'] = serializers.DecimalField(
            min_value=0,
            max_digits=20,
            decimal_places=2,
        )
        self.fields['co2(euro/ton)'] = serializers.DecimalField(
            min_value=0,
            max_digits=20,
            decimal_places=2,
        )
        self.fields['wind(%)'] = serializers.IntegerField(
            min_value=0, max_value=100)


class PowerPlantSerializer(serializers.Serializer):
    name = serializers.CharField()
    type = serializers.ChoiceField(choices=[
        "gasfired", "turbojet", "windturbine"])


class PayLoadSerializer(serializers.Serializer):
    load = serializers.IntegerField(min_value=0)
    fuels = FuelsSerializer()
    powerplants = PowerPlantSerializer(many=True)

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['load'] > 0 and len(data['powerplants']) < 1:
            raise serializers.ValidationError(
                "If load is bigger than 0, then at least "
                " 1 powerplant is required."
            )
        return data
