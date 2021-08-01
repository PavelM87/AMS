from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect


class SuperuserAndLoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'SUP':
            return redirect("landing-page")
        return super().dispatch(request, *args, **kwargs)


class ModeratorAndLoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role not in('MOD', 'SUP'):
            return HttpResponse("Недостаточно прав доступа")
        return super().dispatch(request, *args, **kwargs)

class GuestMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.email == 'guest@test.com':
            return HttpResponse("Недостаточно прав доступа")
        return super().dispatch(request, *args, **kwargs)