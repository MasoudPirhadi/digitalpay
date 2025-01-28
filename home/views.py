import requests
from django.contrib.auth import mixins
from django.contrib.messages import success
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from digitalpay import settings
from home.forms import ProfileForm
from home.models import SideBars


# Create your views here.


class Index(mixins.LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.is_staff:
            return redirect('installments')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        user = request.user.username
        url = "https://api.sms.ir/v1/credit"
        headers = {
            'Accept': 'text/plain',
            "X-API-KEY": settings.SMS_API_KEY
        }
        conn = requests.request(method="GET", url=url, headers=headers)
        if conn.status_code == 200:
            data = conn.json()
            smscount = data['data']
        else:
            smscount = "Error!"
        return render(request, 'home/index.html', {'user': user, "smsCount": smscount})


class Sidebar(View):
    def get(self, request):
        if request.user.is_superuser or request.user.is_staff:
            sidebars = SideBars.objects.filter(is_active=True)
        else:
            sidebars = SideBars.objects.filter(is_active=True).first()
            sidebars = SideBars.objects.filter(is_active=True).exclude(id=sidebars.pk)
        return render(request, 'digitalpay/sidebar.html', {
            'sidebars': sidebars,
        })


class ProfileView(mixins.LoginRequiredMixin, View):
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


class VerifyCode(View):
    def post(self, request):
        url = "https://api.sms.ir/v1/send/verify"
        data = {
            "mobile": "09126515289",
            "templateId": 549059,
            "parameters": [
                {
                    "name": "CODE",
                    "value": "8585"
                }
            ]
        }
        headers = {
            "X-API-KEY": "qkdS9GHskTszxfAlwLtGgb3mm0fKN1k4rdn8t49bzlLezkJ2FgnD143RrFP1frXq"
        }
        key = "qkdS9GHskTszxfAlwLtGgb3mm0fKN1k4rdn8t49bzlLezkJ2FgnD143RrFP1frXq"
        conn = requests.post(url=url, headers=headers, data=data)
        y = conn.request
        print(y)
        return render(request, )
