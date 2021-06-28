from django.shortcuts import render
from django.views.generic import View

class HomePage(View):
	def get(self, request):
		return render(request, "home.html")