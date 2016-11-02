# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from imagekit.admin import AdminThumbnail
from suit_ckeditor.widgets import CKEditorWidget

from .models import Product
from trescec.utils.ckeditor_config import ckeditor_config


class PageForm(ModelForm):
    class Meta:
        widgets = {
            'short_description': CKEditorWidget(editor_options=ckeditor_config),
            'long_description': CKEditorWidget(editor_options=ckeditor_config)
        }

@admin.register(Product)
class DashboardAdmin(admin.ModelAdmin):
    form = PageForm
    search_fields = ['name']
    product_thumbnail = AdminThumbnail(image_field='thumbnail')
    list_display = ['name', 'product_thumbnail', 'price', 'active']
    image_display = AdminThumbnail(image_field='image')
    image_display.short_description = _('Image')
    readonly_fields = ['image_display', 'created', 'modified']
    fields = (
        'active',
        'name',
        'price',
        'short_description',
        'long_description',
        'image',
        'image_display',
        'created',
        'modified'
    )
