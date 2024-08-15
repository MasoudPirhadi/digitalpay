# Generated by Django 5.0.7 on 2024-08-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatar/', verbose_name='تصویر پروفایل'),
        ),
    ]
