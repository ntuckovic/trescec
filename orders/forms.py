# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms import Form, ModelForm

from .models import Order, ShoppingCart


# class ShoppingCartForm(ModelForm):
#     class Meta:
#         model = ShoppingCart
#         fields = [
#             'name',
#             'amount',
#             'monthly_contribution',
#             'wish_date',
#             'photo'
#         ]
