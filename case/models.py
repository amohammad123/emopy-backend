from django.db import models
from utils.models import BaseModel, BaseModelDate


class UserCase(BaseModel, BaseModelDate):
    user = models.ForeignKey(to='account.User', on_delete=models.CASCADE, verbose_name='کاربر',
                             related_name='cases')
    title = models.CharField(max_length=50, verbose_name='عنوان', blank=True, null=True)
    explanation = models.TextField(verbose_name='توضیحات')
    rate = models.PositiveSmallIntegerField(default=5, verbose_name='امتیاز', help_text='از 1 تا 10')
    event = models.ForeignKey(to='event.Event', on_delete=models.CASCADE, verbose_name='رویداد',
                              related_name='cases',
                              blank=True, null=True)

    class Meta:
        verbose_name = 'اتفاق'
        verbose_name_plural = 'اتفاقات'
        db_table = 'user_case'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.user} ==> {self.title}'

