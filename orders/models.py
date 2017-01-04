# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from decimal import Decimal

import time
import hashlib

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.utils.encoding import python_2_unicode_compatible

from constance import config


phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")


def createHash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))

    return hash.hexdigest()[:10]


@python_2_unicode_compatible
class ShoppingCart(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Created'), auto_now_add=True)
    hash = models.CharField(max_length=10, default=createHash, unique=True)
    ordered = models.BooleanField(verbose_name=_('Ordered'), default=False)

    class Meta:
        verbose_name = _('Shopping Cart')
        verbose_name_plural = _('Shopping Carts')

    def __str__(self):
        return self.hash

    def get_items(self):
        return OrderItem.objects.filter(shopping_cart=self)

    @property
    def items_count(self):
        return self.get_items().count()

    @property
    def total_price(self):
        order_items = self.get_items()
        total_price = 0

        for order_item in order_items:
            total_price += order_item.calculated_price

        return total_price

    @property
    def total_and_delivery_price(self):
        calculated = Decimal(self.total_price) + Decimal(config.DELIVERY_PRICE)

        return calculated

    @classmethod
    def create_new(cls):
        shopping_cart = cls()
        shopping_cart.save()

        return shopping_cart


@python_2_unicode_compatible
class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('IP', 'In Progress'),
        ('OR', 'Ordered'),
        ('PR', 'Processed'),
        ('SH', 'Shipped'),
    )
    created = models.DateTimeField(
        verbose_name=_('Created'), auto_now_add=True)
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES,
                              default='IP',)
    finished_on = models.DateTimeField(
        verbose_name=_('Finished on'), blank=True, null=True)
    shipped_on = models.DateTimeField(
        verbose_name=_('Shipped on'), blank=True, null=True)
    first_name = models.CharField(_('First Name'), max_length=150)
    last_name = models.CharField(_('Last Name'), max_length=150)
    place = models.CharField(_('Place'), max_length=200)
    postal_code = models.IntegerField(_('Postal Code'))
    street = models.CharField(_('Street'), max_length=250)
    house_number = models.CharField(
        _('House Number'), max_length=25, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=254)
    phone_number = models.CharField(
        validators=[phone_regex], verbose_name=_('Phone Number'), max_length=15)

    class Meta:
        verbose_name = _('Shop Order')
        verbose_name_plural = _('Shop Orders')

    def __str__(self):
        return self.display_name

    @property
    def display_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    @classmethod
    def get_order_by_shopping_cart(cls, shopping_cart):
        order_items = OrderItem.objects.filter(shopping_cart=shopping_cart)
        order = None

        if order_items:
            order = order_items.first().order

        return order


@python_2_unicode_compatible
class OrderItem(models.Model):
    order = models.ForeignKey('orders.Order', verbose_name=_('Order'), blank=True, null=True)
    shopping_cart = models.ForeignKey(
        'orders.ShoppingCart',
        verbose_name=_('Shopping Cart'),
        blank=True,
        null=True
    )
    product = models.ForeignKey('products.Product', verbose_name=_('Product'))
    amount = models.PositiveIntegerField(verbose_name=_('Amount'))

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')

    def __str__(self):
        return '{0} {1}'.format(self.order, self.product.name)

    @property
    def calculated_price(self):
        return self.amount * self.product.price
