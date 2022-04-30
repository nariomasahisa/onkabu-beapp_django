# Generated by Django 4.0.3 on 2022-04-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onkabu',
            fields=[
                ('id', models.CharField(max_length=48, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('stocks', models.IntegerField(default=0)),
                ('eps', models.FloatField(default=0)),
                ('bps', models.FloatField(default=0)),
                ('devidend', models.FloatField(default=0)),
                ('buy_price', models.IntegerField(default=0)),
                ('total_profit', models.IntegerField(default=0)),
                ('bool_value', models.IntegerField(default=0)),
                ('total_buy_price', models.IntegerField(default=0)),
                ('profit_yield', models.FloatField(default=0)),
                ('roe', models.FloatField(default=0)),
                ('per', models.FloatField(default=0)),
                ('pbr', models.FloatField(default=0)),
            ],
        ),
    ]