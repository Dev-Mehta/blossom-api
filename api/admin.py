from django.contrib import admin

# Register your models here.
from.models import Consumer, Dealer, Plant

admin.site.register(Consumer)
admin.site.register(Dealer)
admin.site.register(Plant)