from api.models import Dealer, Plant

class PlantHelper:
	_plants = None
	filters = []
	# TODO Add plants pagination or dynamic feed load type
	# Currently as the db size is minimal it is feasible to query all
	# plants else it's not a good practice to get all the objects in 
	# single query
	def __init__(self, *args, **kwargs) -> None:
		self._plants = Plant.objects.all()
		if 'supplied_fields' in kwargs.keys():
			filters = kwargs['supplied_fields']

	def get_all_plants(self):
		return self._plants

	def get_plants_by_dealer(self, pat: str):
		dealer_query = Dealer.objects.filter(pat=pat)
		if dealer_query.exists():
			dealer = Dealer.objects.get(pat=pat)
			return dealer.plants
		else:
			return None
	
	def get_plants_by_category(self, category: str):
		return Plant.objects.filter(category=category)

	def get_plant_price_low_to_high(self, category=None, dealer=None):
		plant_query = Plant.objects.all().order_by('-price')
		if category == None and dealer == None:
			pass
		elif category == None:
			dealer_query = Dealer.objects.filter(pat=dealer)
			if dealer_query.exists():
				plant_query = Dealer.objects.get(pat=dealer).plants.order_by('-price')
			else:
				plant_query = []
		elif dealer == None:
			plant_query = Plant.objects.filter(category=category)
		else:
			dealer_query = Dealer.objects.filter(pat=dealer)
			if dealer_query.exists():
				plant_query = Dealer.objects.get(pat=dealer).plants.filter(category=category).order_by('-price')
			else:
				plant_query = []
		return plant_query