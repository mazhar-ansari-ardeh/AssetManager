import datetime

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Asset(models.Model):
    title = models.CharField(max_length=500)
    type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date = models.DateTimeField(default=datetime.datetime.now)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} type {self.type} value {self.amount} owner {self.owner}"

class Liability(models.Model):
    class Meta:
        verbose_name = 'Liability'
        verbose_name_plural = 'Liabilities'
    title = models.CharField(max_length=500)
    type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date = models.DateTimeField(default=datetime.datetime.now)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} type {self.type} value {self.amount} owner {self.owner}"
