# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time
import hashlib

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")


def createHash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))

    return hash.hexdigest()[:10]


class ShoppingCart(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Created'), auto_now_add=True)
    hash = models.CharField(max_length=10, default=createHash, unique=True)

    def __unicode__(self):
        return self.hash


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

    def __unicode__(self):
        return self.display_name

    @property
    def display_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


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

    def __str__(self):
        return '{0} {1}'.format(self.order, self.product.name)

    @property
    def calculated_price(self):
        return self.amount * self.product.price
