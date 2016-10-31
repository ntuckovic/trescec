# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('long_description', models.TextField(verbose_name='Long description')),
                ('image', models.ImageField(upload_to='/products', verbose_name='Image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
    ]