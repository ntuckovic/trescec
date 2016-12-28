# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from imagekit.admin import AdminThumbnail

from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='awesome_ckeditor')
    )
    lead_text = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='awesome_ckeditor')
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    search_fields = ['title']
    list_display = ['title', 'user_id', 'created', 'published', 'modified']
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = _('Image')
    readonly_fields = ['created', 'modified', 'image_display']
    fields = (
        'title',
        'lead_text',
        'content',
        'image',
        'image_display',
        'published',
    )

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user.id
        super(PostAdmin, self).save_model(request, obj, form, change)
