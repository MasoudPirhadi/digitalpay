import uuid

from django.urls import path

from installments import views

urlpatterns = [
    path('', views.Installments.as_view(), name='installments'),
    path('api/<installment_id>/products/', views.Installment_products.as_view(), name='installment_products'),
    path('<installment_id>/', views.InstallmentDetail.as_view(), name='installment_detail'),
]

