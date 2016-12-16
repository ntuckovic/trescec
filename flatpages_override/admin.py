# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.forms import FlatpageForm
from flatblocks.models import FlatBlock

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


class FlatBlockForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='awesome_ckeditor')
    )

    class Meta:
        model = FlatBlock
        fields = ('slug', 'header', 'content')


class FlatBlockAdmin(admin.ModelAdmin):
    form = FlatBlockForm
    ordering = ['slug', ]
    list_display = ('slug', 'header')
    search_fields = ('slug', 'header', 'content')

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, FlatBlockAdmin)
