from plants.helpers import PlantHelper
from api.models import Dealer, Log, Plant
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from django.contrib.auth.models import User
from api.serializers import PlantSerializer
from ipware import get_client_ip
from django.http import HttpRequest
from notifications.signals import notify
class AddPlant(APIView):
	parsers = (JSONParser, MultiPartParser,)
	def put(self, request: HttpRequest, *args, **kwargs):
		if not 'seller_pat' in request.data.keys():
			ip, routable = get_client_ip(request)
			ip = str(ip)
			user_agent = str(request.headers.get('User-Agent'))
			url = request.get_full_path()
			message = "Invalid Plant Access Token Supplied"
			log = Log(url=url, request_method="PUT",
			request_ip=ip, user_agent=user_agent, message=message)
			log.save()
			notify.send(User.objects.get(username='admin'), recipient=User.objects.get(username='admin'), verb=message)
			return JsonResponse({"seller_pat":"This critical field is required. This incident will be reported"})
		seller_exists = Dealer.objects.filter(pat=request.data['seller_pat']).exists()
		if seller_exists:	
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
				seller = Dealer.objects.get(pat=request.data["seller_pat"])
				data = plant_serializer.data
				plant = Plant.objects.get(id=data['id'])
				seller.plants.add(plant)
				seller.save()
				data['created'] = True
				return Response(data)
		else:
			return JsonResponse({"seller_pat":"Invalid critical field supplied. This incident will be reported"})


class FetchAllPlants(APIView):
	def post(self, request, *args, **kwargs):
		plant_helper = PlantHelper(supplied_fields=list(request.data.keys()))
		plant_query = plant_helper.get_all_plants()
		plant_serializer = PlantSerializer(plant_query, many=True)
		return Response(plant_serializer.data)