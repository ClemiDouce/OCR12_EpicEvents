from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from client.models import Client
from userteam.models import Employe


class ContractPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user_team = get_object_or_404(Employe, pk=request.user.id).get_team_name()
        if user_team == "support":
            return False
        client = get_object_or_404(Client, pk=view.kwargs['client_id'])
        if request.method in ["POST", "GET", "PUT", "PATCH"]:
            return client in request.user.client_set.all()
        return False
