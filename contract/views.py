from rest_framework import viewsets

# Create your views here.
from contract.serializers import ContractSerializer


class ContractViewset(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = []