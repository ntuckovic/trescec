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
