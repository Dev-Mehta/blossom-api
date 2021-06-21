from django.http.response import JsonResponse
from api.serializers import ConsumerSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
class RegisterConsumer(APIView):
	def post(self, request, *args, **kwargs):
		user_serializer = UserSerializer(data=request.data)
		consumer_serializer = ConsumerSerializer(data=request.data)
		if user_serializer.is_valid():
			consumer_serializer.is_valid()
			if str(consumer_serializer.errors['user']) == "[ErrorDetail(string='This field is required.', code='required')]" and len(consumer_serializer.errors) == 1:
				user_data = dict(user_serializer.data)
				user = User(username=user_data['username'])
				user.set_password(user_data['password'])
				user.save()
				data = dict(consumer_serializer.data)
				data['user'] = user.id
				tmp_consumer_serializer = ConsumerSerializer(data=data)
				tmp_consumer_serializer.is_valid()
				tmp_consumer_serializer.save()
				user.first_name = data['first_name']
				user.last_name = data['last_name']
				user.email = data['phone_number']
				user.save()
				data['created'] = True
				data['username'] = user_serializer.data.get('username')
				data['user_id'] = user.id
				return JsonResponse(data, status=201)
			else:
				errors = dict(consumer_serializer.errors)
				error_fields = list(errors.keys())
				error_values  = list(errors.values())
				data = {"created":False}
				print(error_fields)
				print(error_values)
				for i in range(0, len(error_values)):
					error_string = str(error_values[i])
					error_string = error_string.split('string=\'')[1].split('\', code=')[0]
					data[error_fields[i]] = error_string
				return JsonResponse(data, status=400)
		else:
			data = {"created":False}
			error_fields = list(user_serializer.errors.keys())
			error_values = list(user_serializer.errors.values())
			for i in range(0, len(error_values)):
				error_string = str(error_values[i])
				error_string = error_string.split('string=\'')[1].split('\', code=')[0]
				data[error_fields[i]] = error_string
			return JsonResponse(data, status=400)
		
class LoginConsumer(APIView):
	def post(self, request, *args, **kwargs):
		data = {'logged_in':False}
		valid_request = True
		if not 'username' in request.data.keys():
			data['username'] = 'This field is required'
			valid_request = False
		if not 'password' in request.data.keys():
			data['password'] = 'This field is required'
			valid_request = False
		if valid_request:
			queried_user = User.objects.filter(username=request.data['username'])
			if queried_user.exists():
				user = User.objects.get(username=request.data['username'])
				valid_password = user.check_password(request.data['password'])
				if valid_password:
					data['logged_in'] = True
					return JsonResponse(data)
				else:
					data['logged_in'] = False
					data['error'] = 'Invalid username or password'
					return JsonResponse(data, status=403)
			else:
				data['username'] = f"User does not exist with username {request.data['username']}"	
				return JsonResponse(data, status=404)	
		else:
			return JsonResponse(data, status=400)