# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from .views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(
        r'^(?P<page>[0-9]+)$',
        PostListView.as_view(),
        name='post_list_paginated'
    ),
    url(r'^post/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post_detail')
]
