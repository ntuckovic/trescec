# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import serializers

from ..models import OrderItem, ShoppingCart


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = (
            'id',
            'hash'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    shopping_cart = ShoppingCartSerializer(required=False)

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'shopping_cart',
            'product',
            'amount'
        )


class ShoppingCartField(serializers.Field):
    def create_shopping_cart(self):
        shopping_cart = ShoppingCart()
        shopping_cart.save()

        return shopping_cart

    def to_representation(self, obj):
        return ShoppingCartSerializer(obj).data

    def to_internal_value(self, data):
        if data is not False:
            shopping_cart = ShoppingCart.objects.filter(
                hash=data
            ).first()
        else:
            shopping_cart = self.create_shopping_cart()

        return shopping_cart


class WriteOrderItemSerializer(OrderItemSerializer):
    shopping_cart = ShoppingCartField(required=False)
