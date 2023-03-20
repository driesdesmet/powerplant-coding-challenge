from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ProductionPlanCreateView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED)
