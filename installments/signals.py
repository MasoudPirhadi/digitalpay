import random
from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

from installments.models import Installment, InstallmentDetail


@receiver(post_save, sender=Installment)
def create_installments(sender, instance: Installment, created, **kwargs):
    if created:
        installment_per_mounth = instance.amount / instance.installments
        for i in range(instance.installments):
            due_date = instance.created_date + timedelta(days=30 * i)
            InstallmentDetail.objects.create(
                id_installment=random.randint(1111111111, 9999999999),
                amount=installment_per_mounth,
                due_date=due_date,
                is_paid=False,
                payment_date=None,
                installments_info=instance
            )

