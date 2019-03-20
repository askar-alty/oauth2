from django.contrib.auth import mixins
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from django.urls import reverse_lazy

from ...accounts.mixins import TwoFactorMixin

LoginRequiredMixin = mixins.LoginRequiredMixin
TwoFactorMixin = TwoFactorMixin


class AuthPermissionRequiredMixin(mixins.PermissionRequiredMixin):
    login_url = reverse_lazy('login')

    def handle_no_permission(self):
        if self.raise_exception and self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('user_does_not_have_permissions', pk=self.request.user.pk)
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())


class UserAuthMixin(AuthPermissionRequiredMixin):
    permission_required = ('sessions.add_session',
                           'sessions.change_session',

                           'oauth2_provider.add_grant',
                           'oauth2_provider.change_grant',

                           'oauth2_provider.add_accesstoken',
                           'oauth2_provider.change_accesstoken')

    def is_from_application(self):
        application = self.get_object()
        if self.request.user.is_superuser:
            return True
        elif application is not None and isinstance(application, Application):
            return application in self.request.user.get_applications()
        else:
            return False

    def has_permission(self):
        return super().has_permission() and self.is_from_application()