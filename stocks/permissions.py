from rest_framework import permissions


class IsStockManOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_stock_man or request.user.is_staff
