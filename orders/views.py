# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic import CreateView, DetailView, TemplateView

from core.views.mixins import NavigationMixin

from .models import ShoppingCart, OrderItem, Order
from .forms import OrderForm


class ShoppingCartMixin(object):
    to_home_if_not_shopping_cart = False
    return_ordered_shopping_cart = False

    def get_shopping_cart_hash(self, request):
        raise NotImplementedError

    def get_shopping_cart(self):
        shopping_cart = ShoppingCart.objects.filter(
            hash=self.shopping_cart_hash,
            ordered=False
        ).first()

        return shopping_cart

    def dispatch(self, request, *args, **kwargs):
        self.shopping_cart_hash = self.get_shopping_cart_hash(request)
        self.shopping_cart = self.get_shopping_cart()

        if self.shopping_cart is None and\
                self.to_home_if_not_shopping_cart is True:
            return HttpResponseRedirect(reverse('flatpages:home'))

        return super(ShoppingCartMixin, self).dispatch(
            request, *args, **kwargs
        )

    def get_context_data(self, **kwargs):
        context_data = super(ShoppingCartMixin, self).get_context_data(
            **kwargs
        )

        context_data['shopping_cart'] = self.shopping_cart
        context_data['order_items'] = OrderItem.objects.select_related(
            'product'
        ).filter(
            shopping_cart=self.shopping_cart
        )

        return context_data


class ShoppingCartView(NavigationMixin, ShoppingCartMixin, TemplateView):
    template_name = 'orders/shoppingcart_detail.html'
    nav_item = 'shopping_cart'

    def get_shopping_cart_hash(self, request):
        return request.COOKIES.get('shopping_cart')

    def get_context_data(self, **kwargs):
        context_data = super(ShoppingCartView, self).get_context_data(**kwargs)
        context_data['amount_range'] = range(1, 101)

        return context_data


class OrderView(NavigationMixin, ShoppingCartMixin, CreateView):
    template_name = 'orders/order_form.html'
    form_class = OrderForm
    nav_item = 'order_form'
    to_home_if_not_shopping_cart = True

    def get_shopping_cart_hash(self, request):
        return self.kwargs.get('cart_hash')

    def get_form_kwargs(self):
        kwargs = super(OrderView, self).get_form_kwargs()
        kwargs['shopping_cart'] = self.shopping_cart

        return kwargs

    def get_success_url(self):
        return reverse('orders:order_success', kwargs={
            'cart_hash': self.shopping_cart.hash
        })


class SuccessView(NavigationMixin, ShoppingCartMixin, TemplateView):
    nav_item = 'order_form'
    template_name = 'orders/order_sent.html'
    to_home_if_not_shopping_cart = True

    def get_shopping_cart_hash(self, request):
        return self.kwargs.get('cart_hash')

    def get_shopping_cart(self):
        shopping_cart = ShoppingCart.objects.filter(
            hash=self.shopping_cart_hash,
            ordered=True
        ).first()

        return shopping_cart

    def get_context_data(self, **kwargs):
        self.order = Order.get_order_by_shopping_cart(self.shopping_cart)

        if not self.order or self.order.status != 'OR':
            return HttpResponseRedirect(reverse('flatpages:home'))

        context_data = super(SuccessView, self).get_context_data(**kwargs)
        context_data['order'] = self.order

        return context_data
