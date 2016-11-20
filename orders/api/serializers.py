# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import serializers

from ..models import OrderItem, ShoppingCart


class ShoppingCartSerializer(serializers.ModelSerializer):
    items_count = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = (
            'id',
            'hash',
            'items_count'
        )

    def get_items_count(self, obj):
        return OrderItem.objects.filter(shopping_cart=obj).count()


class OrderItemSerializer(serializers.ModelSerializer):
    shopping_cart = ShoppingCartSerializer(required=False)

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'product',
            'amount',
            'calculated_price',
            'shopping_cart',
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

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True

        super(WriteOrderItemSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        existing_order_item = OrderItem.objects.filter(
            product=validated_data.get('product'),
            shopping_cart=validated_data.get('shopping_cart')
        ).first()

        if existing_order_item:
            existing_order_item.amount += validated_data.get("amount", 0)

            existing_order_item.save()

            instance = existing_order_item
        else:
            instance = super(WriteOrderItemSerializer, self).create(
                validated_data
            )

        return instance
