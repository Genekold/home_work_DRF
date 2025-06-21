from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверка является ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """Проверка является ли пользователь создателем курса/урока."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
