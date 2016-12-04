# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from .models import Order, OrderItem, ShoppingCart


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'product'
    ]


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'place', 'street']
    list_display = [
        'display_name',
        'email',
        'phone_number',
        'status'
    ]
    inlines = [
        OrderItemInline
    ]


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = [
        'hash',
        'created'
    ]
    inlines = [
        OrderItemInline
    ]
