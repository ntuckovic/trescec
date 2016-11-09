# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('orders.api.urls', namespace='api', app_name='orders')),
]
