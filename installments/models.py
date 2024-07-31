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
    Installment_id = models.BigIntegerField(verbose_name='شناسه اقساط', unique=True, blank=True, auto_created=True, editable=False)
    amount = models.BigIntegerField(verbose_name='مبلغ')
    created_date = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    is_done = models.BooleanField(verbose_name='اتمام اقساط', default=False)

    def __str__(self):
        return str(self.Installment_id)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.Installment_id is None:
            self.Installment_id = random.randint(1, 9999999999)
            return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

