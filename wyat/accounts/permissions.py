from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsAnonCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated():
            return True
        elif request.method != 'POST' and not request.user.is_authenticated():
            return True
        elif request.method in SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated():
            return False
        if request.method in SAFE_METHODS:
            return True

        return obj.username == request.user.username