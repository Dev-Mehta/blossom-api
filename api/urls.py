from django.urls import path, include

urlpatterns = [
	path('consumer/', include('consumer.urls')),
	path('seller/', include('seller.urls')),
	# path('plants/', include('plants.urls')),
]