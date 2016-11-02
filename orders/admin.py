# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'place', 'street']
    list_display = [
        'display_name',
        'email',
        'phone_number',
        'status'
    ]


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = [
        'order',
        'product'
    ]
