# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from .views import ProductListView, ProductDetailView

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^(?P<page>[0-9]+)$', ProductListView.as_view(), name='product_list_paginated'),
    url(r'^product/(?P<pk>[0-9]+)$', ProductDetailView.as_view(), name='product_detail')
]
