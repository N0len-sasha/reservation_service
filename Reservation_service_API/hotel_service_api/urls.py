from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    RoomViewSet,
    ReservationViewSet
)

s_router_v1 = SimpleRouter()
s_router_v1.register(r'rooms',
                     RoomViewSet,
                     basename='rooms')
s_router_v1.register(r'bookings',
                     ReservationViewSet,
                     basename='bookings')

urlpatterns = [
    path('', include(s_router_v1.urls)),
]