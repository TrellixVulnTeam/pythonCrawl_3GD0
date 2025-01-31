# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-16 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qmf_api', '0002_orderlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='beizhu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='beizhu'),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='beizhu2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='beizhu2'),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='order_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='pay_money',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='金额'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='trade_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='支付状态'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='trade_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='支付类型'),
        ),
    ]
