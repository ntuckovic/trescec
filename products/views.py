# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()

        qs = qs.filter(active=True)

        return qs

    def get_context_data(self, **kwargs):
        context_data = super(ProductListView, self).get_context_data(**kwargs)

        context_data['amount_range'] = range(1, 101)

        return context_data
