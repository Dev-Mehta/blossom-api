from . import views
from django.urls import path

urlpatterns = [
	path('get-plants/', views.FetchAllPlants.as_view())
]