from django.contrib import admin

from home.models import SideBars


# Register your models here.

@admin.register(SideBars)
class SideBarsAdmin(admin.ModelAdmin):
    pass

