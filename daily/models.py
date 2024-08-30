from django.db import models

from utils.models import BaseModel, BaseModelDate
from utils.time import time_now


class Therapy(BaseModel, BaseModelDate):
    user = models.ForeignKey(to='account.User', on_delete=models.CASCADE, verbose_name='کاربر',
                             related_name='therapies')
    therapist = models.ForeignKey(to='account.User', on_delete=models.CASCADE, verbose_name='درمانگر',
                                  related_name='therapist')
    start_time = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='زمان شروع جلسه')
    duration = models.PositiveIntegerField(default=45, verbose_name='مدت زمان جلسه', help_text='به دقیقه')
    cost = models.PositiveIntegerField(verbose_name='هزینه جلسه', help_text='به تومان', blank=True, null=True)
    rate = models.PositiveSmallIntegerField(default=5, verbose_name='امتیاز', help_text='از 1 تا 10')
    canceled = models.BooleanField(default=False, verbose_name='لغو شده')
    before_emotion = models.TextField(verbose_name='احساسات قبل از شروع جلسه', blank=True, null=True)
    after_emotion = models.TextField(verbose_name='احساسات پس از برگزاری جلسه', blank=True, null=True)

    class Meta:
        verbose_name = 'جلسه درمان'
        verbose_name_plural = 'جلسات درمان'
        db_table = 'therapy'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.user}'


class DailyReport(BaseModel, BaseModelDate):
    user = models.ForeignKey(to='account.User', on_delete=models.CASCADE, verbose_name='کاربر',
                             related_name='reports')
    sleep_start_time = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='زمان شروع خواب')
    sleep_duration = models.PositiveIntegerField(blank=True, null=True, verbose_name='مدت زمان خواب',
                                                 help_text='به دقیقه')
    sleep_rate = models.PositiveSmallIntegerField(default=5, verbose_name='امتیاز کیفیت خواب', help_text='از 1 تا 10')

    mood = models.TextField(blank=True, null=True, verbose_name='مود')
    functional_rate = models.PositiveSmallIntegerField(default=5, verbose_name='امتیاز عملکرد', help_text='از 1 تا 10')
    is_rest = models.BooleanField(default=False, verbose_name='استراحت')
    emotion_explanation = models.TextField(verbose_name='احساسات روز', blank=True, null=True)

    class Meta:
        verbose_name = 'گزارش روزانه'
        verbose_name_plural = 'گزارشات روزانه'
        db_table = 'daily_report'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.user}'
