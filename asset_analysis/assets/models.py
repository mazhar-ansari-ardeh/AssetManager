import datetime

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

class Stock(models.Model):
    title = models.CharField(max_length=500)
    type = models.CharField(max_length=28, default='Stock')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_obtained = models.DateTimeField(default=datetime.datetime.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    symbol = models.CharField(max_length=500)
    quantity = models.IntegerField()

# class Stock(Asset):
#     asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE, to_fields="id")

    # def __str__(self):
    #     return f"{self.symbol} value {self.amount}"
