# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label=_('Contact name'))
    contact_email = forms.EmailField(required=True, label=_('Contact email'))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label=_('Content')
    )

    def send_email(self):
        msg_txt = render_to_string(
            'core/contact_message.txt',
            {
                'contact_name': self.cleaned_data.get('contact_name'),
                'contact_email': self.cleaned_data.get('contact_email'),
                'content':  self.cleaned_data.get('content'),
            }
        )

        email = send_mail(
            subject=_('Contact from {0}').format(
                self.cleaned_data.get('contact_email')
            ),
            from_email=settings.SHOP_SYSTEM_EMAIL,
            recipient_list=settings.SHOP_CONTACT_EMAILS,
            message=msg_txt,
        )

        return email
