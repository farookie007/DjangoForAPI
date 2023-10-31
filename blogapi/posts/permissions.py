from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # handles permission for POST and the SAFE methods
        # only authenticated users cant access listview
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # handles permissions for all SaFE methods and other methods
        # except POST method
        if request.method  in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed for the author of the post
        return request.user == obj.author