import random

from django.db import models

from account.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام کالا')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return f"{self.name} ( {self.count} عدد )"


class Installment(models.Model):
    user = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE)
    product_name = models.ManyToManyField(to=Product, max_length=200, verbose_name='نام کالا')
    Installment_id = models.BigIntegerField(verbose_name='شناسه اقساط', unique=True, blank=True, auto_created=True, editable=False, db_index=True)
    amount = models.BigIntegerField(verbose_name='مبلغ')
    installments = models.IntegerField(verbose_name='تعداد اقساط', default=12)
    created_date = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    is_done = models.BooleanField(verbose_name='اتمام اقساط', default=False)

    def __str__(self):
        return str(self.Installment_id)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.Installment_id is None:
            self.Installment_id = random.randint(1, 9999999999)
            return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class InstallmentDetail(models.Model):
    installments_info = models.ForeignKey(Installment, on_delete=models.CASCADE, verbose_name='اطلاعات اقساط')
    id_installment = models.BigIntegerField(verbose_name='شناسه قسط', unique=True, auto_created=True, editable=False, db_index=True)
    due_date = models.DateField(verbose_name='تاریخ سررسید')
    payment_date = models.DateField(verbose_name='تاریخ پرداخت', blank=True, null=True)
    amount = models.BigIntegerField(verbose_name='مبلغ هر قسط')
    is_paid = models.BooleanField(verbose_name='پرداخت شده', default=False)

    def __str__(self):
        return self.id_installment

