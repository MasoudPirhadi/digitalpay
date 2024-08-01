# Generated by Django 5.0 on 2024-07-31 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SideBars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.CharField(blank=True, max_length=100, unique=True, verbose_name='عنوان در url')),
                ('icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='آیکون')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت')),
            ],
        ),
    ]
