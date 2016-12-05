# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.forms import FlatpageForm
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PageForm(FlatpageForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='awesome_ckeditor')
    )


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    form = PageForm
    fieldsets = [
        (None, {'fields': ('sites', 'title', 'content')}),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': (
                'url',
                # 'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    ]

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
