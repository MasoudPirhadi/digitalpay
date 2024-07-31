from django.contrib import admin

from installments.models import Installment, Product


# Register your models here.


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ['Installment_id', 'user', 'created_date']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
