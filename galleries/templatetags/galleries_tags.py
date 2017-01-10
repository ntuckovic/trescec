# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import Gallery

register = template.Library()


@register.assignment_tag
def get_gallery_by_name(name):
    return Gallery.objects.filter(name=name).first()
