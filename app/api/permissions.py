from rest_framework import permissions

class IsReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return  request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return  request.method in permissions.SAFE_METHODS



class IsAuthor(permissions.BasePermission):
    """
    Only allow the owner of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsSelf(permissions.BasePermission):
    """
    Only currently logged in user can:
    - edit their profile
    - follow and unfollow new people
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user




