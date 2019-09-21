from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class FinanceType(models.Model):
    class Meta:
        verbose_name = '记账类名'
        verbose_name_plural = '记账类名' 

    Name = models.CharField(max_length=200 , verbose_name='名称')
    CreateDate = models.DateTimeField('创建时间',default = timezone.now)
    def __str__(self):
        return self.Name