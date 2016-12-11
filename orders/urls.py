# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include

from .views import ShoppingCartView, OrderView, SuccessView

urlpatterns = [
    url(r'^shopping-cart/$', ShoppingCartView.as_view(), name='shopping_cart'),
    url(r'^order/(?P<cart_hash>\w+)/$', OrderView.as_view(), name='order_form'),
    url(r'^order/(?P<cart_hash>\w+)/sent$', SuccessView.as_view(), name='order_success'),
    url(r'^api/', include('orders.api.urls', namespace='api', app_name='orders')),
]
