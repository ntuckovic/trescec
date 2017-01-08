# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.forms import TextInput

from imagekit.admin import AdminThumbnail

from .models import Gallery, Image


class ImageInline(admin.TabularInline):
    model = Image
    formfield_overrides = {
        models.PositiveIntegerField: {'widget': TextInput(attrs={'class': 'input_sm_number'})},
    }
    readonly_fields = ['admin_thumbnail']
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    admin_thumbnail.short_description = _('Preview')

    fields = (
        'title',
        'image',
        'admin_thumbnail',
        'ordering',
    )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        'name', 'items_count', 'created',
    ]
    readonly_fields = ['created']
    fields = (
        'name',
        'created',
    )
    inlines = [
        ImageInline
    ]

    def items_count(self, obj):
        return obj.items_count

    items_count.short_description = _('Items Count')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ['title']
    image_thumbnail = AdminThumbnail(image_field='thumbnail')
    list_display = [
        'title', 'image_thumbnail', 'gallery',
    ]
    image_display = AdminThumbnail(image_field='image')
    image_display.short_description = _('Image')
    readonly_fields = ['image_display', 'created']
    fields = (
        'title',
        'image',
        'image_display',
        'ordering',
        'gallery',
        'created',
    )
