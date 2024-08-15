from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse


class RediretToHome(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('installments'))
        else:
            return super().dispatch(request, *args, **kwargs)