# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal

from django import template

from orders.models import ShoppingCart

from constance import config

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_shopping_cart(context):
    shopping_cart_hash = context.get('request').COOKIES.get("shopping_cart")
    shopping_cart = None

    if shopping_cart_hash:
        shopping_cart = ShoppingCart.objects.filter(
            hash=shopping_cart_hash,
            ordered=False
        ).first()

    return shopping_cart


@register.simple_tag
def get_delivery_price():
    delivery_price = Decimal(config.DELIVERY_PRICE)

    return delivery_price
