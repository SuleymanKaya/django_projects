from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "You must be owner of this object"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
        
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

    