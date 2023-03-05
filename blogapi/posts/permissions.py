from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """Only authenticated users can see list view."""
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        """Read permissions are allowed to any request so we'll always allow GET, HEAD, or OPTIONS requests."""
        return (request.method in permissions.SAFE_METHODS) or (obj.author == request.user)