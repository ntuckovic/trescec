# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import serializers

from django.utils.translation import ugettext as _

from products.api.serializers import LightProductSerializer
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


class FullOrderItemSerializer(OrderItemSerializer):
    product = LightProductSerializer()


class ShoppingCartField(serializers.Field):
    def create_shopping_cart(self):
        return ShoppingCart.create_new()

    def to_representation(self, obj):
        return ShoppingCartSerializer(obj).data

    def to_internal_value(self, data):
        if data is not False:
            shopping_cart = ShoppingCart.objects.filter(
                hash=data,
                ordered=False
            ).first()

            if shopping_cart is None:
                shopping_cart = self.create_shopping_cart()
        else:
            shopping_cart = self.create_shopping_cart()

        return shopping_cart


class WriteOrderItemSerializer(OrderItemSerializer):
    shopping_cart = ShoppingCartField(required=False)

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True

        super(WriteOrderItemSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        product = data.get('product')

        if product is not None:
            if product.available is False or product.active is False:
                raise serializers.ValidationError(
                    _('This product can not be added to shopping cart')
                )

        return data

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

    def to_representation(self, instance):
        return FullOrderItemSerializer().to_representation(instance)
