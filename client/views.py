from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import get_object_or_404

from client.models import Client
from client.permissions import ClientPermission
from client.serializers import ClientSerializer
from userteam.models import Employe


class ClientViewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [ClientPermission]

    def get_queryset(self):
        user_team = get_object_or_404(Employe, pk=self.request.user.id).team.name.lower()
        if user_team == "support":
            list_client = set(self.request.user.event_set.values_list('client', flat=True))
            return Client.objects.filter(id__in=list_client)
        elif user_team == "sales":
            return Client.objects.filter(salesContact=self.request.user)
        return False

    def perform_create(self, serializer):
        serializer.save(salesContact=self.request.user)
