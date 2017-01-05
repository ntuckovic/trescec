# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Product(models.Model):
    ordering = models.PositiveIntegerField(verbose_name=_('Ordering'), default=0)
    name = models.CharField(verbose_name=_('Name'), max_length=500)
    short_description = models.TextField(verbose_name=_('Short Description'), blank=True, null=True)
    long_description = models.TextField(verbose_name=_('Long Description'), blank=True, null=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='products/', blank=True, null=True)
    created = models.DateTimeField(
        verbose_name=_('Created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Modified'), auto_now=True)
    price = models.DecimalField(
        verbose_name=_('Price'), max_digits=10, decimal_places=2)
    available = models.BooleanField(verbose_name=_('Available'), default=True)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(100, 100)],
                               format='JPEG',
                               options={'quality': 100})
    medium_thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(400)],
                               format='JPEG',
                               options={'quality': 100})

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['ordering', '-id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        now = timezone.now()

        self.modified = now

        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id])
