from django.urls import path
from . import views
from plants import views as plant_views
urlpatterns = [
	path('register/', views.RegisterDealer.as_view()),
	path('login/', views.LoginDealer.as_view()),
	path('add-plant/', plant_views.AddPlant.as_view()),
]