# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.utils.encoding import python_2_unicode_compatible

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=500)
    lead_text = models.TextField(verbose_name=_('Lead Text'))
    content = models.TextField(verbose_name=_('Content'))
    published = models.BooleanField(verbose_name=_('Published'), default=False)
    created = models.DateTimeField(
        verbose_name=_('Created'), auto_now_add=True)
    modified = models.DateTimeField(
        verbose_name=_('Modified'), auto_now_add=True)
    published_on = models.DateTimeField(
        verbose_name=_('Published on'), blank=True, null=True)
    user_id = models.PositiveIntegerField(verbose_name=_('User ID'))
    image = models.ImageField(
        verbose_name=_('Image'), upload_to='posts/', blank=True, null=True)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(500, 500)],
                                      format='JPEG',
                                      options={'quality': 100})

    class Meta:
        verbose_name = _('Post')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = timezone.now()

        self.modified = now

        if self.published is True:
            self.published_on = now

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogs:post_detail', args=[self.id])
