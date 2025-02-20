from rest_framework import viewsets
from .models import Room, Reservation
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .serializers import RoomSerializer, ReservationSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('price', 'create_date')


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('date_start')
    serializer_class = ReservationSerializer
