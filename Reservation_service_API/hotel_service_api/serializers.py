from rest_framework import serializers
from .models import Room, Reservation


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        print(data)
        if data['date_start'] > data['date_end']:
            raise serializers.ValidationError("Дата окончания должна быть не раньше даты начала")
        return data

    def to_representation(self, instance):
        if self.context.get('request').method == 'POST':
            return {'id': instance.id}
        return super().to_representation(instance)


class RoomSerializer(serializers.ModelSerializer):
    recipes = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'price', 'description', 'create_date', 'recipes')

    def to_representation(self, instance):
        if self.context.get('request').method == 'POST':
            return {'id': instance.id}
        return super().to_representation(instance)