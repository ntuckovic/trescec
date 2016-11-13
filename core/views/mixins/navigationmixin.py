# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class NavigationMixin(object):
    nav_item = ''

    def get_context_data(self, **kwargs):
        context_data = super(NavigationMixin, self).get_context_data(**kwargs)

        context_data['nav_item'] = self.nav_item

        return context_data
