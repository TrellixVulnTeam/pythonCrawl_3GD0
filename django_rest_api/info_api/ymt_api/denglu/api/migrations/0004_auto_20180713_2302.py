# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-13 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_useradmin_reqmid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradmin',
            name='url',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='url'),
        ),
    ]
