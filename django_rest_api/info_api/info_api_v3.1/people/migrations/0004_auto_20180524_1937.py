# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-24 11:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20180524_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='join_time',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='join_time',
            name='join_time',
            field=models.CharField(choices=[('1', '1小时'), ('2', '2小时'), ('3', '3小时'), ('4', '4小时'), ('6', '6小时')], max_length=3, verbose_name='参与时间'),
        ),
    ]
