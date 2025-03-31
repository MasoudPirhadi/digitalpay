import requests
from django.shortcuts import render, redirect
from django.views import View

from digitalpay import settings


# Create your views here.


class SmsPanel(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.is_staff:
            return redirect('installments')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        headers = {
            'Accept': 'application/json',
            "X-API-KEY": settings.SMS_API_KEY
        }
        # for credit
        url_credit = "https://api.sms.ir/v1/credit"
        connect_credit = requests.request(method="GET", url=url_credit, headers=headers)
        if connect_credit.status_code == 200:
            data = connect_credit.json()
            smscount = data['data']
        else:
            smscount = "Error!"

        # for lines
        url_line = "https://api.sms.ir/v1/line"
        connect_line = requests.request(method="GET", url=url_line, headers=headers)
        if connect_credit.status_code == 200:
            data = connect_line.json()
            lines = data['data']
        else:
            lines = "Error!"

        url_report_today = "https://api.sms.ir/v1/send/live"
        connect_report_today = requests.request(method="GET", url=url_report_today, headers=headers)
        if connect_report_today.status_code == 200:
            data = connect_report_today.json()
            report_today = data['data']
        else:
            report_today = "Error!"

        return render(request, 'sms_panel/sms_panel.html', {
            "smscount": smscount,
            "lines": lines,
            "report_today": report_today,
        })
