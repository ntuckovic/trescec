# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms import Form, ModelForm

from .models import Order, ShoppingCart


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'place',
            'postal_code',
            'street',
            'house_number',
            'email',
            'phone_number'
        ]

    def __init__(self, *args, **kwargs):
        self.shopping_cart = kwargs.pop('shopping_cart')

        super(OrderForm, self).__init__(*args, **kwargs)
