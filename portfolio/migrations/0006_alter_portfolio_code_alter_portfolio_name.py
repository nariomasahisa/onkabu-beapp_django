# Generated by Django 4.0.3 on 2022-05-01 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_portfolio_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='code',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
