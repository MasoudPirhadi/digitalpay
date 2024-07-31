from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import TemplateView

from account.models import User
from home.models import SideBars


# Create your views here.


class Index(View):
    def get(self, request):
        user = request.user.username
        return render(request, 'home/index.html', {'user': user})


def sidebar(request):
    sidebars = SideBars.objects.filter(is_active=True)
    return render(request, 'digitalpay/sidebar.html', {
        'sidebars': sidebars,
    })


