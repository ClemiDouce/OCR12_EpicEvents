import logging

from django.http import Http404
from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import get_object_or_404

from client.models import Client
from event.models import Event
from event.permissions import EventPermission
from event.serializers import EventSerializer
from userteam.models import Employe

logger = logging.getLogger(__name__)


class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [EventPermission]

    def get_queryset(self):
        user_team = get_object_or_404(Employe, pk=self.request.user.id).team.name.lower()
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        if user_team == "support":
            queryset = client.event_set.filter(supportContact=self.request.user)
        elif user_team == "sales":
            queryset = client.event_set.all()
        else:
            return False

        client_name = self.request.query_params.get('name')
        client_email = self.request.query_params.get('email')
        contract_date = self.request.query_params.get('date')
        if client_name is not None:
            queryset = queryset.filter(client__lastName=client_name)
        if client_email is not None:
            queryset = queryset.filter(client__email=client_email)
        if contract_date is not None:
            queryset = queryset.filter(dateCreated=contract_date)

        return queryset

    def perform_create(self, serializer):
        try:
            client = get_object_or_404(Client, pk=self.kwargs['client_id'])
            serializer.save(client=client)
        except Http404:
            logger.debug("Client not found")


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
