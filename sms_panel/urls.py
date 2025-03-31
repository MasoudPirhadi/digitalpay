from django.urls import path

from . import views

urlpatterns = [
    path('', views.SmsPanel.as_view(), name='sms_panel'),
]