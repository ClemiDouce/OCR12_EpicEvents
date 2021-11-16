from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import get_object_or_404

from client.models import Client
from contract.models import Contract
from contract.permissions import ContractPermission
from contract.serializers import ContractSerializer


class ContractViewset(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [ContractPermission]

    def get_queryset(self):
        """Renvoie la liste des contrats du clients"""
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        return client.contract_set.filter(saleContact=self.request.user)

    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        serializer.save(saleContact=self.request.user, client=client)


class SelfContractViewset(viewsets.ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.filter(saleContact=self.request.user)
