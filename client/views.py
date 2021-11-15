from rest_framework import viewsets

# Create your views here.
from client.models import Client
from client.serializers import ClientSerializer


class ClientViewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()