from dataclasses import fields
from email.policy import default
import imp
from rest_framework import serializers
from portfolio.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = [
            'id',
            'code',
            'name',
            'stocks',
            'eps',
            'bps',
            'devidend',
            'buy_price',
            'total_profit',
            'book_value',
            'total_buy_price',
            'profit_yield',
            'roe',
            'per',
            'pbr',
            'uid'
        ]

# class PortfolioSerializer(serializers.Serializer):
#   id = serializers.ImageField(read_only=True)
#   code = serializers.CharField(max_length=4, default='')
#   name = serializers.CharField(max_length=50, default='')
#   stocks = serializers.ImageField()
#   eps = serializers.FloatField()
#   bps = serializers.FloatField()
#   devidend = serializers.FloatField()
#   buy_price = serializers.ImageField()
#   total_profit = serializers.ImageField()
#   book_value = serializers.ImageField()
#   total_buy_price = serializers.ImageField()
#   profit_yield = serializers.FloatField()
#   roe = serializers.FloatField()
#   per = serializers.FloatField()
#   pbr = serializers.FloatField()
#   uid = serializers.CharField(max_length=48, default='')

#   def create(self, validated_data):
#       return Portfolio.objects.create(**validated_data)

#   def update(self,instance, validated_data):
#       instance.code = validated_data.get('code',instance.code)
#       instance.name = validated_data.get('name', instance.name)
#       instance.stocks = validated_data.get('stocks', instance.stocks)
#       instance.eps = validated_data.get('eps', instance.eps)
#       instance.bps = validated_data.get('bps', instance.bps)
#       instance.devidend = validated_data.get('devidend', instance.devidend)
#       instance.buy_price = validated_data.get('buy_price', instance.buy_price)
#       instance.total_profit = validated_data.get('total_profit', instance.total_profit)
#       instance.total_buy_price = validated_data.get('total_buy_price', instance.total_buy_price)
#       instance.book_value = validated_data.get('book_value', instance.book_value)
#       instance.total_buy_price = validated_data.get('total_buy_price', instance.total_buy_price)
#       instance.profit_yield = validated_data.get('profit_yield', instance.profit_yield)
#       instance.roe = validated_data.get('roe', instance.roe)
#       instance.per = validated_data.get('per', instance.per)
#       instance.pbr = validated_data.get('pbr', instance.pbr)
#       instance.uid = validated_data.get('uid', instance.uid)
#       return instance