from rest_framework import viewsets

# Create your views here.
from rest_framework.generics import get_object_or_404

from client.models import Client
from contract.models import Contract
from contract.serializers import ContractSerializer


class ContractViewset(viewsets.ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        client = get_object_or_404(Client, pk=client_id)
        return Contract.objects.filter(client=client)

class SelfContractViewset(viewsets.ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(saleContact=user)