# Generated by Django 5.0.7 on 2025-03-31 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='تصویر پروفایل'),
        ),
    ]
