from rest_framework import viewsets

# Create your views here.
from event.serializers import EventSerializer


class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = []