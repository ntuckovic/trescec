# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from core.views.mixins import NavigationMixin
from .models import Post


class PostMixin(NavigationMixin, object):
    model = Post
    nav_item = 'blog'

    def get_queryset(self):
        qs = super(PostMixin, self).get_queryset()

        qs = qs.filter(published=True)

        return qs


class PostListView(PostMixin, ListView):
    paginate_by = 10
    pass


class PostDetailView(PostMixin, DetailView):
    pass
