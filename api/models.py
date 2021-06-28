from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from hashlib import sha256
# Create your models here.
class Consumer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	street_address = models.CharField(max_length=500)
	city = models.CharField(max_length=300)
	state = models.CharField(max_length=300)
	postal_code = models.CharField(max_length=15)
	phone_number = models.CharField(max_length=13)

	@property
	def full_name(self):
		return self.first_name + " " + self.last_name
	
	def __str__(self) -> str:
		return self.full_name

	"""
	@docstring sample request
	{
		"first_name":"Dev",
		"last_name":"Mehta",
		"street_address":"Nikunj, Madhav Park, Near Tagore Society",
		"city":"Surendranagar",
		"state":"Gujarat",
		"postal_code":"363001",
		"phone_number":"+918200280632"
	}
	"""

class Dealer(models.Model):
	def generate_pat(phone_number):
		return sha256(str(phone_number).encode()).hexdigest()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	street_address = models.CharField(max_length=500)
	city = models.CharField(max_length=300)
	state = models.CharField(max_length=300)
	postal_code = models.CharField(max_length=15)
	phone_number = models.CharField(max_length=13)
	bio = models.CharField(max_length=200)
	is_verified = models.BooleanField(default=False)
	plants = models.ManyToManyField('Plant',blank=True)
	pat = models.CharField(max_length=64, default=generate_pat(phone_number))
		
	@property
	def full_name(self):
		return self.first_name + " " + self.last_name

	@property
	def verified(self):
		return self.is_verified
	
	def __str__(self) -> str:
		return self.full_name


class Plant(models.Model):
	class Category(models.TextChoices):
		HERB = "HERB", "Herb"
		SHRUB = "SHRUB", "Shrub"
		TREE = "TREE", "Tree"
		CLIMBER = "CLIMBER", "Climber"
		CREEPER = "CREEPER", "Creeper"
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.PositiveIntegerField()
	cover_image = models.ImageField(upload_to=settings.MEDIA_ROOT,blank=True)
	category = models.CharField(choices=Category.choices,default=Category.HERB, max_length=15)

	def __str__(self) -> str:
		return f"{self.name}, Type: {self.category}"

class Log(models.Model):
	url = models.CharField(max_length=500)
	request_method = models.CharField(max_length=200)
	request_ip = models.CharField(max_length=100)
	user_agent = models.CharField(max_length=300)
	message = models.TextField()
	logging_time = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return f"{self.message[:50]} | {self.logging_time}"