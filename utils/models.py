from django.db import models
from .time import time_now
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='شناسه')

    create_date = models.BigIntegerField(default=time_now, editable=False, verbose_name='تاریخ ایجاد')

    update_date = models.BigIntegerField(default=time_now, verbose_name='تاریخ ویرایش')

    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.update_date = time_now()

        return super(BaseModel, self).save(*args, **kwargs)


class BaseModelDate(models.Model):
    day = models.SmallIntegerField(verbose_name='روز')

    month = models.SmallIntegerField(verbose_name='ماه')

    year = models.SmallIntegerField(verbose_name='سال')

    class Meta:
        abstract = True
