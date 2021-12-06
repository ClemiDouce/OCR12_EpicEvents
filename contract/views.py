import logging

from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import get_object_or_404

from client.models import Client
from contract.models import Contract
from contract.permissions import ContractPermission
from contract.serializers import ContractSerializer

logger = logging.getLogger(__name__)


class ContractViewset(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [ContractPermission]

    def get_queryset(self):
        """Renvoie la liste des contrats du clients"""
        logger.warning('Comment ca va la mif')
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        return client.contract_set.filter(saleContact=self.request.user)

    def perform_create(self, serializer):
        try:
            client = Client.objects.get(pk=self.kwargs['client_id'])
            serializer.save(saleContact=self.request.user, client=client)
        except Client.DoesNotExist:
            logger.warning("Client not found")


class SelfContractViewset(viewsets.ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        queryset = Contract.objects.filter(saleContact=self.request.user)
        client_name = self.request.query_params.get('name')
        client_email = self.request.query_params.get('email')
        contract_date = self.request.query_params.get('date')
        contract_amount = self.request.query_params.get('amount')
        if client_name is not None:
            queryset = queryset.filter(client__lastName=client_name)
        if client_email is not None:
            queryset = queryset.filter(client__email=client_email)
        if contract_date is not None:
            queryset = queryset.filter(dateCreated=contract_date)
        if contract_amount is not None:
            queryset = queryset.filter(amount=contract_amount)
        return queryset
