import logging

from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import get_object_or_404

from client.models import Client
from client.permissions import ClientPermission
from client.serializers import ClientSerializer
from userteam.models import Employe

logger = logging.getLogger(__name__)

class ClientViewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [ClientPermission]

    def get_queryset(self):
        user_team = get_object_or_404(Employe, pk=self.request.user.id).get_team_name()
        if user_team == "support":
            list_client = set(self.request.user.event_set.values_list('client', flat=True))
            queryset = Client.objects.filter(id__in=list_client)
        elif user_team == "sales":
            queryset = Client.objects.filter(salesContact=self.request.user)
        else:
            return False
        client_name = self.request.query_params.get('name')
        client_email = self.request.query_params.get('email')
        if client_name is not None:
            queryset = queryset.filter(lastName=client_name)
        if client_email is not None:
            queryset = queryset.filter(email=client_email)
        return queryset

    def perform_create(self, serializer):
        serializer.save(salesContact=self.request.user)
