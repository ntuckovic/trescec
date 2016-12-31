# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse, reverse_lazy

from core.views.mixins import NavigationMixin
from core.forms import ContactForm


class ContactView(NavigationMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    nav_item = 'contact'

    def form_valid(self, form):
        self.sent_data = form.send_email()

        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return '{0}?contact_email={1}&contact_name={2}'.format(
                reverse('contact_email_sent'),
                self.sent_data.get('contact_email'),
                self.sent_data.get('contact_name'),
            )


class ContactEmailSent(NavigationMixin, TemplateView):
    template_name = 'contact_email_sent.html'
    form_class = ContactForm
    nav_item = 'contact'


class HomepageView(NavigationMixin, TemplateView):
    template_name = 'homepage.html'
    nav_item = 'home'

    def get_context_data(self, **kwargs):
        context_data = super(HomepageView, self).get_context_data(
            **kwargs
        )

        context_data['contact_form'] = ContactForm

        return context_data
