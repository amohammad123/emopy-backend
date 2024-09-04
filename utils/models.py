from django.db import models
from .time import time_now, get_shamsi
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
    day = models.SmallIntegerField(verbose_name='روز', default=int(get_shamsi().get('day')))

    month = models.SmallIntegerField(verbose_name='ماه', default=int(get_shamsi().get('month')))

    year = models.SmallIntegerField(verbose_name='سال', default=int(get_shamsi().get('year')))

    detail = models.JSONField(verbose_name='جزئیات', blank=True, null=True)

    stamp_date = models.PositiveBigIntegerField(default=time_now, verbose_name='تاریخ تایم استمپ')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.detail = get_shamsi().get('time')
        return super(BaseModelDate, self).save(*args, **kwargs)

