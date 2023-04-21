from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to allow only creators of an object to edit / delete
    the said object. Assumes that the model instance has an 'Author' attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Always allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Instance must have an attribute named 'Author'
        return obj.author == request.user