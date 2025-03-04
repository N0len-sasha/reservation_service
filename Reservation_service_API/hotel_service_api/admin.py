from django.contrib import admin

from hotel_service_api.models import Reservation, Room

admin.site.register(Room)
admin.site.register(Reservation)
