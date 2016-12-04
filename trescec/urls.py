# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.flatpages import views


urlpatterns = [
    url(r'^$', views.flatpage, {'url': '/'}, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls', namespace='products',
        app_name='products')),
    url(r'^orders/', include('orders.urls', namespace='orders',
        app_name='orders')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
