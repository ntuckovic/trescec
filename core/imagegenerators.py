# -*- coding: utf-8 -*-

from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill, ResizeToFit


class SmallThumbnail(ImageSpec):
    processors = [ResizeToFill(300, 300)]
    format = 'JPEG'
    options = {'quality': 100}


class MediumThumbnail(SmallThumbnail):
    processors = [ResizeToFill(500, 500)]


class LargeThumbnail(SmallThumbnail):
    processors = [ResizeToFill(900, 900)]


class SmallThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=300)]


class MediumThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=500)]

class LargeThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=900)]

register.generator('small_thumbnail', SmallThumbnail)
register.generator('medium_thumbnail', MediumThumbnail)
register.generator('large_thumbnail', LargeThumbnail)
register.generator('small_thumbnail_fit', SmallThumbnailFit)
register.generator('medium_thumbnail_fit', MediumThumbnailFit)
register.generator('large_thumbnail_fit', LargeThumbnailFit)
