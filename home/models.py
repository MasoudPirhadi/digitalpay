from django.db import models


# Create your models here.

class SideBars(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.CharField(max_length=100, verbose_name='عنوان در url', unique=True, blank=True, help_text='اگر قصد دارید فقط همین URL باشد حتما قبل و بعد آن "/" قرار دهید.')
    icon = models.CharField(verbose_name="آیکون", max_length=50, blank=True, null=True)
    position = models.IntegerField(verbose_name="ترتیب نمایش", max_length=50)
    is_active = models.BooleanField(default=True, verbose_name='وضعیت')

    def __str__(self):
        return self.title
