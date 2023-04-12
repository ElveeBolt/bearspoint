from django.http import Http404
from django.contrib.auth.mixins import UserPassesTestMixin


class UserCheckAdministratorMixin(UserPassesTestMixin):
    """
    Mixin of check type user.
    """
    def test_func(self):
        return self.request.user.groups.filter(name='administrator').exists()

    def handle_no_permission(self):
        raise Http404('User type is not administrator')