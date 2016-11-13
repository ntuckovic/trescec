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
    queryset = OrderItem.objects.all()
    permission_classes = []
