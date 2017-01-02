# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from imagekit.admin import AdminThumbnail

from .models import Product
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PageForm(forms.ModelForm):
    short_description = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='awesome_ckeditor'),
        label=_('Short Description')
    )
    long_description = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='awesome_ckeditor'),
        label=_('Long Description')
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
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
