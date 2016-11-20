# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include

from .views import ShoppingCartView

urlpatterns = [
    url(r'^shopping-cart/$', ShoppingCartView.as_view(), name='shopping_cart'),
    url(r'^api/', include('orders.api.urls', namespace='api', app_name='orders')),
]
