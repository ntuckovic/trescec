# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from django import forms

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
    readonly_fields = ['created', 'modified']
    fields = (
        'title',
        'lead_text',
        'content',
        'published',
    )

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user.id
        super(PostAdmin, self).save_model(request, obj, form, change)
