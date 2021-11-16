from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import get_object_or_404

from client.models import Client
from event.models import Event
from event.permissions import EventPermission
from event.serializers import EventSerializer
from userteam.models import Employe


class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [EventPermission]

    def get_queryset(self):
        user_team = get_object_or_404(Employe, pk=self.request.user.id).team.name.lower()
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        if user_team == "support":
            return client.event_set.filter(supportContact=self.request.user)
        elif user_team == "sales":
            return client.event_set.all()
        return False

    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        serializer.save(client=client)


class SelfEventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = []

    def get_queryset(self):
        user_team = get_object_or_404(Employe, pk=self.request.user.id).team.name.lower()
        if user_team == "support":
            return Event.objects.filter(supportContact=self.request.user)
        elif user_team == "sales":
            client_list = self.request.user.client_set.all()
            return Event.objects.filter(client__in=client_list)
