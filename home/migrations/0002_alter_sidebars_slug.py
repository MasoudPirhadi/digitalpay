# Generated by Django 5.0.6 on 2024-07-17 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebars',
            name='slug',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='عنوان در url'),
        ),
    ]
