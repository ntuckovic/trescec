# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.assignment_tag
def get_thumbnail_url(generatedimage):
    thumbnail_url = ''

    try:
        thumbnail_url = generatedimage.url
    except:
        thumbnail_url = ''

    return thumbnail_url
