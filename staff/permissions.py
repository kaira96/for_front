from rest_framework import permissions


class IsAccountantOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_accountant or request.user.is_staff
