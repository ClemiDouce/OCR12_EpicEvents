from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from userteam.models import Employe


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return


    def has_object_permission(self, request, view, obj):
        user_team = get_object_or_404(Employe, pk=request.user).team.name.lower()
        if user_team == "support":
            list_client = set(request.user.event_set.values_list('client', flat=True))
            if request.method == "GET" and obj.pk in list_client:
                return True
        elif user_team == "sales":
            if request.method in ["PUT", "PATCH", "GET"]:
                if obj in request.user.client_set.all():
                    return True
                return False