# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from .views import ProductListView

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product-list'),
]
