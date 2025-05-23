from django.urls import include, path
from rest_framework.routers import SimpleRouter

from hotel_service_api.views import ReservationViewSet, RoomViewSet

s_router_v1 = SimpleRouter()
s_router_v1.register(r"rooms", RoomViewSet, basename="rooms")
s_router_v1.register(r"bookings", ReservationViewSet, basename="bookings")

urlpatterns = [
    path("", include(s_router_v1.urls)),
]
