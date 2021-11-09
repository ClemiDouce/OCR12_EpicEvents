from rest_framework import viewsets

# Create your views here.
from client.serializers import ClientSerializer


class ClientViewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = []