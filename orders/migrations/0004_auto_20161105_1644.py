# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20161102_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Amount'),
        ),
    ]