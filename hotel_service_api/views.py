from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from hotel_service_api.models import Reservation, Room
from hotel_service_api.serializers import ReservationSerializer, RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ("price", "create_date")

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"id": response.data["id"]}, status=status.HTTP_201_CREATED)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by("date_start")
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"id": response.data["id"]}, status=status.HTTP_201_CREATED)
