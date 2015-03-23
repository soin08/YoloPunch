from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if  request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Only allow current user to edit their profile.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user

