# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20161101_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
