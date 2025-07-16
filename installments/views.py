from django.contrib.auth import mixins
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from installments.models import Installment


# Create your views here.


class Installments(mixins.LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser or request.user.is_staff:
            installments = Installment.objects.all().order_by('is_done')
        else:
            installments = Installment.objects.filter(user_id=request.user.id).order_by('is_done')
        return render(request, 'installments/installments.html', {
            'installments': installments,
        })


class Installment_products(mixins.LoginRequiredMixin, View):
    def get(self, request, installment_id):
        installment = get_object_or_404(Installment, Installment_id=installment_id)
        products = installment.product_name.all()
        product_list = [{'name': product.name, 'count': product.count} for product in products]
        return JsonResponse({
            'products': product_list
        })


class InstallmentDetail(mixins.LoginRequiredMixin, View):
    def get(self, request, installment_id):
        installment = get_object_or_404(Installment, Installment_id=installment_id, is_done=False)
        return render(request, 'installments/installment_detail.html', {
            'installment': installment
        })
