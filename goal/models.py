from django.db import models
from utils.models import BaseModel, BaseModelDate


class Goal(BaseModel, BaseModelDate):

    user = models.ForeignKey(to='account.User', on_delete=models.CASCADE, verbose_name='کاربر',
                             related_name='goals')
    title = models.CharField(max_length=50, verbose_name='عنوان', blank=True, null=True)
    note = models.TextField(verbose_name='توضیح', blank=True, null=True)
    is_completed = models.BooleanField(default=True, verbose_name='کامل شده')
    image = models.ImageField(upload_to='event_images', verbose_name='تصویر', blank=True, null=True)
    due_date = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='زمان رسیدن به هدف')

    class Meta:
        verbose_name = 'هدف'
        verbose_name_plural = 'اهداف'
        db_table = 'goal'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.user}'

