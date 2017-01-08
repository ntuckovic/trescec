# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from constance import config
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


@python_2_unicode_compatible
class Gallery(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Created'), auto_now_add=True)
    name = models.CharField(_('Name'), max_length=250)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __str__(self):
        return self.name

    @property
    def items(self):
        gallery_items = Image.objects.filter(gallery=self)

        return gallery_items

    @property
    def items_count(self):
        return self.items.count()


@python_2_unicode_compatible
class Image(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Created'), auto_now_add=True)
    title = models.CharField(
        verbose_name=_('Title'), max_length=500, default='')
    image = models.ImageField(
        verbose_name=_('Image'), upload_to='galleries/')
    ordering = models.PositiveIntegerField(
        verbose_name=_('Ordering'), default=0)
    gallery = models.ForeignKey(
        'galleries.Gallery', verbose_name=_('Gallery'), blank=True, null=True)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFit(width=150)],
                               format='JPEG',
                               options={'quality': 100})

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering = ['gallery', 'ordering', '-id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if config.SET_DEFAULT_GALLERY is True and self.gallery is None:
            gallery = Gallery.objects.filter(
                name=config.DEFAULT_GALLERY_NAME
            ).first()

            self.gallery = gallery

        super(Image, self).save(*args, **kwargs)
