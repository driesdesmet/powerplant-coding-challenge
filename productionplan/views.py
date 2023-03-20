from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PayLoadSerializer


class ProductionPlanCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PayLoadSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
