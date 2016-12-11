# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.flatpages import views


urlpatterns = [
    url(r'^$', views.flatpage, {'url': '/'}, name='home'),
    url(r'^about/$', views.flatpage, {'url': '/about/'}, name='about'),
]
