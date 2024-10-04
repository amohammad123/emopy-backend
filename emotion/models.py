from django.db import models
from utils.models import BaseModel, BaseModelDate


class Emotion(BaseModel):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(verbose_name='تصویر', upload_to='emotion_images', null=True, blank=True)
    color = models.CharField(max_length=10, blank=True, null=True, verbose_name='کد رنگ')

    class Meta:
        verbose_name = 'احساس'
        verbose_name_plural = 'احساسات'
        db_table = 'emotion'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.title}'


class UserEmotion(BaseModel, BaseModelDate):
    user = models.ForeignKey(to='account.User', on_delete=models.CASCADE, verbose_name='کاربر',
                             related_name='emotions')
    rate = models.PositiveSmallIntegerField(default=5, verbose_name='امتیاز', help_text='از 1 تا 10')
    event = models.ForeignKey(to='event.Event', on_delete=models.CASCADE, verbose_name='رویداد',
                              related_name='emotions',
                              blank=True, null=True)
    emotion = models.ForeignKey(to=Emotion, on_delete=models.CASCADE, verbose_name='احساس',
                                related_name='users_emotion')

    class Meta:
        verbose_name = 'احساس کاربر'
        verbose_name_plural = 'احساسات کاربر'
        db_table = 'user_emotion'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.user}'


class Mood(BaseModel):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    image = models.ImageField(verbose_name='تصویر', upload_to='mood', null=True, blank=True)
    color = models.CharField(max_length=10, blank=True, null=True, verbose_name='کد رنگ')
    sort = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'مود'
        verbose_name_plural = 'مودها'
        db_table = 'mood'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.user}'