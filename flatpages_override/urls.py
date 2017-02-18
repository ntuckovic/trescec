# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.flatpages import views


urlpatterns = [
    url(
        r'^ljekovitost-aronije/$',
        views.flatpage, {'url': '/ljekovitost-aronije/'},
        name='ljekovitost-aronije'
    ),
]
