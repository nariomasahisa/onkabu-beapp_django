import code
from pyexpat import model
from statistics import mode
from django.db import models

class Portfolio(models.Model):
  id = models.CharField(max_length=48, unique=True, primary_key=True, null=False)
  code = models.CharField(max_length=4, null=False)
  name = models.CharField(max_length=50, null=False)
  stocks = models.IntegerField(default=0, null=False)
  eps = models.FloatField(default=0, null=False)
  bps = models.FloatField(default=0, null=False)
  devidend = models.FloatField(default=0, null=False)
  buy_price = models.IntegerField(default=0, null=False)
  total_profit = models.IntegerField(default=0, null=False)
  bool_value = models.IntegerField(default=0, null=False)
  total_buy_price = models.IntegerField(default=0, null=False)
  profit_yield = models.FloatField(default=0, null=False)
  roe = models.FloatField(default=0, null=False)
  per = models.FloatField(default=0, null=False)
  pbr = models.FloatField(default=0, null=False)