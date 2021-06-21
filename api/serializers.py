from rest_framework import serializers
from .models import Consumer, Dealer, Plant
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password')

class ConsumerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Consumer
		fields = "__all__"

class DealerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dealer
		fields = "__all__"

class PlantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plant
		fields = "__all__"