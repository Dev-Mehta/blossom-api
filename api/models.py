from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
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
	@property
	def full_name(self):
		return self.first_name + " " + self.last_name

	@property
	def verified(self):
		return self.is_verified
	
	def __str__(self) -> str:
		return self.full_name

class Plant(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.PositiveIntegerField()
	cover_image = models.ImageField(upload_to=settings.MEDIA_ROOT,blank=True)
