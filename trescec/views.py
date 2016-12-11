# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from core.views.mixins import NavigationMixin
from core.forms import ContactForm


class ContactView(NavigationMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    # success_url = reverse('email_sent')
    nav_item = 'contact'

    def form_valid(self, form):
        form.send_email()

        return super(ContactView, self).form_valid(form)
