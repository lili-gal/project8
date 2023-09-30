from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moder').exists() or request.user.is_staff:
            return True
        print(view.get_object().users.filter(id='3'))
        if view.get_object().users.filter(id=request.user.id).exists():
            return True
        else:
            return False
