from rest_framework import viewsets

# Create your views here.
from event.models import Event
from event.serializers import EventSerializer


class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = []
    queryset = Event.objects.all()

class SelfEventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = []
    def get_queryset(self):
        print(self.request.user)
        return Event.objects.filter(supportContact=self.request.user)