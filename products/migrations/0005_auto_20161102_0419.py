# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 03:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='status',
            new_name='active',
        ),
    ]