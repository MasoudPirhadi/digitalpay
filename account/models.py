from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.CharField(verbose_name='نام کاربری', max_length=100, unique=True)
    phone = models.IntegerField(verbose_name='موبایل')

    def __str__(self):
        return str(self.phone)

