from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from api.serializers import PlantSerializer

class AddPlant(APIView):
	parsers = (JSONParser, MultiPartParser,)
	def put(self, request, *args, **kwargs):
		plant_serializer = PlantSerializer(data=request.data)
		if not plant_serializer.is_valid():
			errors = dict(plant_serializer.errors)
			error_fields = list(errors.keys())
			error_values  = list(errors.values())
			data = {"created":False}
			for i in range(0, len(error_values)):
				error_string = str(error_values[i])
				error_string = error_string.split('string=\'')[1].split('\', code=')[0]
				data[error_fields[i]] = error_string
			return JsonResponse(data)
		else:
			plant_serializer.save()
			data = plant_serializer.data
			data['created'] = True
			return Response(data)