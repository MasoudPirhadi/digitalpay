from django.contrib import messages
from django.contrib.messages import SUCCESS, success
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import TemplateView

from account.models import User
from home.forms import ProfileForm
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


class ProfileView(View):
    def get(self, request: HttpRequest):
        form = ProfileForm(instance=request.user)
        return render(request, 'home/profile.html', {'form': form})

    def post(self, request: HttpRequest):
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            success(request, 'اطلاعات شما با موفقیت بروز شدند.')
            return redirect('profile')
        return render(request, 'home/profile.html', {'form': form})

