# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill


class ListThumbnail(ImageSpec):
    processors = []
    format = 'JPEG'
    options = {'quality': 100}

register.generator('products:list:thumbnail', ListThumbnail)
