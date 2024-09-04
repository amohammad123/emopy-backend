from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.models import BaseModel, BaseModelDate
from utils.time import time_now


class User(BaseModel, AbstractUser):
    username = models.CharField(verbose_name='تلفن همراه', max_length=11, unique=True)
    image = models.ImageField(verbose_name='تصویر', upload_to='user_images', null=True, blank=True)
    is_therapist = models.BooleanField(default=False, verbose_name='درمانگر')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        db_table = 'user'
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.username}'


class PhoneCode(BaseModel):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_active = models.BooleanField(default=False)
    expire_date = models.PositiveBigIntegerField()
    code = models.CharField(max_length=5, editable=False)

    class Meta:
        verbose_name = 'کد تایید'
        verbose_name_plural = 'کدهای تایید'
        db_table = 'phone_code'

    def __str__(self):
        return f'USER: {self.user} ==> {self.code}'

    def save(self, *args, **kwargs):
        if not self.code:
            # self.code = generate_code()
            self.code = 12345
        if not self.expire_date:
            self.expire_date = time_now() + 20
        return super(PhoneCode, self).save(*args, **kwargs)

