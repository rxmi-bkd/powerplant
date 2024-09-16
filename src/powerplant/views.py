from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from powerplant.serializers import EnergyLoadRequestSerializer
from .utils import compute_production_plan


@api_view(['POST'])
@parser_classes([JSONParser])
def get_production_plan(request):
	serializer = EnergyLoadRequestSerializer(data = request.data)

	if serializer.is_valid():
		load = serializer.validated_data['load']
		fuels = serializer.validated_data['fuels']
		powerplants = serializer.validated_data['powerplants']

		production_plan = compute_production_plan(load, fuels, powerplants)
		return Response(production_plan)

	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

