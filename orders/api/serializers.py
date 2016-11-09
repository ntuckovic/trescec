# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import serializers

from ..models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'shopping_cart',
            'product',
            'amount'
        )
