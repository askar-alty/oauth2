from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import PermissionRequiredMixin

from .tow_factor import TwoFactorMixin

TwoFactorMixin = TwoFactorMixin


class RolePermissionRequiredMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('login')

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            return redirect('user_does_not_have_permissions', pk=self.request.user.pk)
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())


class RoleCreationMixin(RolePermissionRequiredMixin):
    permission_required = ('accounts.add_role',)


class RoleChangeMixin(RolePermissionRequiredMixin):
    permission_required = ('accounts.change_role',)


class RoleViewMixin(RolePermissionRequiredMixin):
    permission_required = ('accounts.view_role',)


class RoleDeleteMixin(RolePermissionRequiredMixin):
    permission_required = ('accounts.delete_role',)