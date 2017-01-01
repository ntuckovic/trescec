# -*- coding: utf-8 -*-

from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill, ResizeToFit


class ExtraSmallThumbnail(ImageSpec):
    processors = [ResizeToFill(150, 150)]
    format = 'JPEG'
    options = {'quality': 100}


class SmallThumbnail(ExtraSmallThumbnail):
    processors = [ResizeToFill(300, 300)]


class MediumThumbnail(SmallThumbnail):
    processors = [ResizeToFill(500, 500)]


class BigThumbnail(SmallThumbnail):
    processors = [ResizeToFill(700, 700)]


class LargeThumbnail(SmallThumbnail):
    processors = [ResizeToFill(900, 900)]


class ExtraSmallThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=150)]


class SmallThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=300)]


class MediumThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=500)]


class GreatThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=600)]


class BigThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=700)]


class LargeThumbnailFit(SmallThumbnail):
    processors = [ResizeToFit(width=900)]

register.generator('extrasmall_thumbnail', ExtraSmallThumbnail)
register.generator('small_thumbnail', SmallThumbnail)
register.generator('medium_thumbnail', MediumThumbnail)
register.generator('big_thumbnail', BigThumbnail)
register.generator('large_thumbnail', LargeThumbnail)

register.generator('extrasmall_thumbnail_fit', ExtraSmallThumbnailFit)
register.generator('small_thumbnail_fit', SmallThumbnailFit)
register.generator('medium_thumbnail_fit', MediumThumbnailFit)
register.generator('great_thumbnail_fit', GreatThumbnailFit)
register.generator('big_thumbnail_fit', BigThumbnailFit)
register.generator('large_thumbnail_fit', LargeThumbnailFit)
