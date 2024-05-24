from rest_framework.permissions import BasePermission,SAFE_METHODS
from authUser.models import Teacher
class AssignmentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if Teacher.objects.filter(user=self.request.user).exists():
            return True
        return request.user in SAFE_METHODS or request.user.is_superuser  or request.user.is_staff

    