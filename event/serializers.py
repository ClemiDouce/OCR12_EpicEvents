from rest_framework import serializers

from .models import Event, EventStatus


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = '__all__'
