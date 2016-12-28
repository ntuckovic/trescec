# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import serializers

from ..models import Product


class LightProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'active'
        )
