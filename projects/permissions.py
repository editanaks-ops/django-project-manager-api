from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Разрешаем чтение всем
        if request.method in SAFE_METHODS:
            return True

        # Разрешаем только staff (админ/менеджер)
        return request.user and request.user.is_staff