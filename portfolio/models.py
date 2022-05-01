from datetime import datetime
from django.db import models

class Portfolio(models.Model):

  # テーブルのカラムの設定
  id = models.AutoField(primary_key=True)
  code = models.CharField(max_length=4, null=False, default='')
  name = models.CharField(max_length=50, null=False, default='')
  stocks = models.IntegerField(default=0, null=False)
  eps = models.FloatField(default=0, null=False)
  bps = models.FloatField(default=0, null=False)
  devidend = models.FloatField(default=0, null=False)
  buy_price = models.IntegerField(default=0, null=False)
  total_profit = models.IntegerField(default=0, null=False)
  book_value = models.IntegerField(default=0, null=False)
  total_buy_price = models.IntegerField(default=0, null=False)
  profit_yield = models.FloatField(default=0, null=False)
  roe = models.FloatField(default=0, null=False)
  per = models.FloatField(default=0, null=False)
  pbr = models.FloatField(default=0, null=False)
  uid = models.CharField(max_length=48, null=False, default='')