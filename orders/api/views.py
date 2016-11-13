# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import viewsets

from core.api.mixins import ReadWriteSerializerMixin

from ..models import OrderItem
from .serializers import OrderItemSerializer, WriteOrderItemSerializer


class OrderItemViewSet(ReadWriteSerializerMixin, viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing order items.
    """
    list_serializer = OrderItemSerializer
    write_serializer = WriteOrderItemSerializer
    permission_classes = []

    def get_queryset(self):
        shopping_cart = self.request.COOKIES.get('shopping_cart')
        show_all = self.request.GET.get('show_all')

        if show_all:
            return OrderItem.objects.all()
        elif show_all is None and shopping_cart:
            return OrderItem.objects.filter(shopping_cart__hash=shopping_cart)
        else:
            return OrderItem.objects.none()
