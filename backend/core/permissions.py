"""
JurisAgenda - Permission Classes (RBAC)
Roles: ADMIN, LAWYER, SECRETARY, TV_OPERATOR
"""
from rest_framework.permissions import BasePermission

from accounts.models import RoleChoices


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.role == RoleChoices.ADMIN
        )


class IsAdminOrLawyer(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role in (RoleChoices.ADMIN, RoleChoices.LAWYER)
        )


class IsAdminOrLawyerOrSecretary(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role in (
                RoleChoices.ADMIN, RoleChoices.LAWYER, RoleChoices.SECRETARY
            )
        )


class IsTVOperator(BasePermission):
    """TV_OPERATOR só pode acessar o painel TV — não cria/edita eventos."""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role == RoleChoices.TV_OPERATOR
        )


class CannotModifyEvents(BasePermission):
    """
    Regras de acesso para eventos:
    - Não autenticado → 401
    - TV_OPERATOR → só leitura (GET/HEAD/OPTIONS)
    - ADMIN, LAWYER, SECRETARY → acesso completo
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.role == RoleChoices.TV_OPERATOR:
            return request.method in ("GET", "HEAD", "OPTIONS")
        return request.user.role in (
            RoleChoices.ADMIN, RoleChoices.LAWYER, RoleChoices.SECRETARY
        )
