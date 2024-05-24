from rest_framework.permissions import BasePermission,SAFE_METHODS

class ResultPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser