from django.db import models
from utils.models import BaseModel, BaseModelDate


class ImportantDay(BaseModel, BaseModelDate):
    user = models.ForeignKey(to='account.User', on_delete=models.CASCADE, verbose_name='کاربر',
                             related_name='importants')
    title = models.CharField(max_length=50, verbose_name='عنوان', blank=True, null=True)
    note = models.TextField(verbose_name='توضیح', blank=True, null=True)
    image = models.ImageField(upload_to='event_images', verbose_name='تصویر', blank=True, null=True)
    date = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'روز مهم'
        verbose_name_plural = 'روز های مهم'
        db_table = 'importantDay'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.user}'

