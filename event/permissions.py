from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from userteam.models import Employe


class EventPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user_team = get_object_or_404(Employe, pk=request.user.id).team.name.lower()
        # client = get_object_or_404(Client, pk=view.kwargs['client_id'])
        if user_team == "sales":
            return request.method in ["POST", "GET"]
        elif user_team == "support":
            return request.method in ["PUT", "PATCH", "GET"]
        return False

    def has_object_permission(self, request, view, obj):
        # user_team = get_object_or_404(Employe, pk=request.user.id).team.name.lower()
        if request.method in ["PUT", "PATCH"]:
            return obj.eventStatus_id != 2
