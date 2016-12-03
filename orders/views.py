# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin, TemplateResponseMixin
# from django.views.generic import FormView
# from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView, DetailView

from core.views.mixins import NavigationMixin

from .models import ShoppingCart, OrderItem
from .forms import OrderForm


class ShoppingCartView(NavigationMixin, TemplateView):
    template_name = 'orders/shoppingcart_detail.html'
    nav_item = 'shopping_cart'

    def dispatch(self, request, *args, **kwargs):
        self.shopping_cart_hash = self.request.COOKIES.get('shopping_cart')
        self.shopping_cart = ShoppingCart.objects.filter(
            hash=self.shopping_cart_hash
        ).first()

        return super(ShoppingCartView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(ShoppingCartView, self).get_context_data(**kwargs)

        context_data['shopping_cart'] = self.shopping_cart
        context_data['order_items'] = OrderItem.objects.select_related(
            'product'
        ).filter(
            shopping_cart=self.shopping_cart
        )

        context_data['amount_range'] = range(1, 101)
        context_data['shopping_cart'] = self.shopping_cart

        return context_data


class OrderView(NavigationMixin, CreateView):
    template_name = 'orders/order_form.html'
    form_class = OrderForm
    nav_item = 'order_form'

    def dispatch(self, request, *args, **kwargs):
        self.shopping_cart_hash = self.kwargs.get('cart_hash')
        self.shopping_cart = ShoppingCart.objects.filter(
            hash=self.shopping_cart_hash
        ).first()

        if self.shopping_cart is None:
            return HttpResponseRedirect(reverse('home'))

        return super(OrderView, self).dispatch(
            request, *args, **kwargs
        )

    def get_form_kwargs(self):
        kwargs = super(OrderView, self).get_form_kwargs()
        kwargs['shopping_cart'] = self.shopping_cart

        return kwargs
