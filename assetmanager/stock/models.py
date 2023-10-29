from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Asset(models.Model):
    category = models.ForeignKey(Category, related_name='assets', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    quantity = models.FloatField()
    created_by = models.ForeignKey(User, related_name='assets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Stock(Asset):
    ticker = models.CharField(max_length=255)
    purchase_price = models.FloatField()
    purchased_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

# class Cash(Asset):
#
#     def __str__(self):
#         return self.name
