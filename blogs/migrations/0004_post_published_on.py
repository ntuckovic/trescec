# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Published on'),
        ),
    ]
