from django.urls import path
from . import views
urlpatterns = [
	path('register/', views.RegisterConsumer.as_view()),
	path('login/', views.LoginConsumer.as_view()),
]