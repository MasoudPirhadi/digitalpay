# Generated by Django 5.0.6 on 2024-07-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installments', '0004_remove_installment_installment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installment',
            name='payment_id',
        ),
        migrations.AddField(
            model_name='installment',
            name='Installment_id',
            field=models.BigIntegerField(auto_created=True, blank=True, default=1, editable=False, unique=True, verbose_name='شناسه اقساط'),
            preserve_default=False,
        ),
    ]