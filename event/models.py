from django.db import models
from utils.models import BaseModel, BaseModelDate


class Event(BaseModel, BaseModelDate):
    START = (
        (0, 'فکر'),
        (1, 'احساس'),
        (2, 'اتفاق')
    )
    user = models.ForeignKey(to='account.User', on_delete=models.CASCADE, verbose_name='کاربر',
                             related_name='events')
    title = models.CharField(max_length=50, verbose_name='عنوان', blank=True, null=True)
    note = models.TextField(verbose_name='یادداشت', blank=True, null=True)
    response = models.TextField(verbose_name='پاسخ', blank=True, null=True)
    analyze = models.TextField(verbose_name='تحلیل', blank=True, null=True)
    result = models.TextField(verbose_name='نتیجه', blank=True, null=True)
    start_status = models.CharField(max_length=10, choices=START, verbose_name='وضعیت شروع', default=0)
    is_completed = models.BooleanField(default=True, verbose_name='کامل شده')
    image = models.ImageField(upload_to='event_images', verbose_name='تصویر', blank=True, null=True)
    brief_explanation = models.TextField(verbose_name='توضیح مختصر', blank=True, null=True)
    mood = models.ForeignKey(to='emotion.Mood', on_delete=models.CASCADE, related_name='events',
                             verbose_name='مود')

    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = 'رویدادها'
        db_table = 'event'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.user}'
