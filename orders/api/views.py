# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import viewsets

from ..models import OrderItem
from .serializers import OrderItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing order items.
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = []
