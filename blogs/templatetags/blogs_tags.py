# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


from ..models import Post


@register.assignment_tag
def get_last_n_posts(number=1):
    posts = Post.objects.all()

    return {
        'posts': posts[:number],
        'count': posts.count()
    }
