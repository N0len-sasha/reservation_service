from rest_framework import serializers

from hotel_service_api.models import Reservation, Room


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        print(data)
        if data["date_start"] > data["date_end"]:
            raise serializers.ValidationError(
                "Дата окончания должна быть не раньше даты начала"
            )
        return data


class RoomSerializer(serializers.ModelSerializer):
    recipes = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ("id", "price", "description", "create_date", "recipes")
