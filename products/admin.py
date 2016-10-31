# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from imagekit.admin import AdminThumbnail
from suit_ckeditor.widgets import CKEditorWidget

from .models import Product

toolbarGroups = [
		{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] },
		{ 'name': 'clipboard', 'groups': [ 'clipboard', 'undo' ] },
		{ 'name': 'editing', 'groups': [ 'find', 'selection', 'spellchecker', 'editing' ] },
		{ 'name': 'forms', 'groups': [ 'forms' ] },
		{ 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ] },
		{ 'name': 'paragraph', 'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi', 'paragraph' ] },
		{ 'name': 'links', 'groups': [ 'links' ] },
		{ 'name': 'insert', 'groups': [ 'insert' ] },
		{ 'name': 'styles', 'groups': [ 'styles' ] },
		{ 'name': 'colors', 'groups': [ 'colors' ] },
		{ 'name': 'tools', 'groups': [ 'tools' ] },
		{ 'name': 'others', 'groups': [ 'others' ] },
		{ 'name': 'about', 'groups': [ 'about' ] }
	];

removeButtons = 'Flash,ShowBlocks,About,Scayt,TextField,Radio,Checkbox,Form,Textarea,Button,Select,HiddenField,ImageButton,SelectAll,Find,Replace,Print,Preview,NewPage,Save,Templates,CreateDiv,Language,BidiRtl,BidiLtr';


class PageForm(ModelForm):
    class Meta:
        widgets = {
            'short_description': CKEditorWidget(editor_options={
                'startupFocus': True,
                'toolbarGroups': toolbarGroups,
                'removeButtons': removeButtons
            }),
            'long_description': CKEditorWidget(editor_options={
                'startupFocus': True,
                'toolbarGroups': toolbarGroups,
                'removeButtons': removeButtons
            })
        }

@admin.register(Product)
class DashboardAdmin(admin.ModelAdmin):
    form = PageForm
    search_fields = ['name']
    product_thumbnail = AdminThumbnail(image_field='thumbnail')
    list_display = ['name', 'product_thumbnail', 'price']
    image_display = AdminThumbnail(image_field='image')
    image_display.short_description = _('Image')
    readonly_fields = ['image_display', 'created', 'modified']
    fields = (
        'name',
        'price',
        'short_description',
        'long_description',
        'image',
        'image_display',
        'created',
        'modified'
    )
