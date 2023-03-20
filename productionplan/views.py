from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PayLoadSerializer, ProductionPlanItemSerializer


def compute_productionplan(payload):
    powerplants = payload['powerplants']

    # Compute effective_power and cost_per_MWh
    for powerplant in powerplants:
        if powerplant['type'] == 'windturbine':
            powerplant['cost_per_MWh'] = 0
            powerplant['effective_max'] = powerplant['pmax'] * payload["fuels"]["wind(%)"] / 100
        if powerplant['type'] == 'gasfired':
            powerplant['cost_per_MWh'] = payload['fuels']["gas(euro/MWh)"] / powerplant['efficiency']
            powerplant['effective_max'] = powerplant['pmax']
        if powerplant['type'] == 'turbojet':
            powerplant['cost_per_MWh'] = payload['fuels']["kerosine(euro/MWh)"] / powerplant['efficiency']
            powerplant['effective_max'] = powerplant['pmax']

    # Sort the powerplants according to cost_per_MWh (merit order)
    powerplants.sort(key=lambda x: x['cost_per_MWh'])

    # Compute output power per powerplant and add them to a production plan list
    total_power = 0
    production_plan = []
    for powerplant in powerplants:
        power = min(powerplant["effective_max"], payload['load'] - total_power)
        total_power += power
        production_plan.append({
            "name": powerplant["name"],
            "p": power
        })

    return production_plan


class ProductionPlanCreateView(APIView):
    def post(self, request, *args, **kwargs):
        payload_serializer = PayLoadSerializer(data=request.data)
        if payload_serializer.is_valid():
            production_plan = compute_productionplan(payload_serializer.validated_data)
            pp_serializer = ProductionPlanItemSerializer(production_plan, many=True)
            return Response(data=pp_serializer.data, status=status.HTTP_201_CREATED)
        return Response(payload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
