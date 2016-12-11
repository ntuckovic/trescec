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


class ShoppingCartMixin(object):
    is_new_shopping_cart = False

    def get_shopping_cart_hash(self, request):
        raise NotImplementedError

    def get_new_shopping_cart(self):
        self.is_new_shopping_cart = True

        return ShoppingCart.create_new()

    def get_shopping_cart(self, request, shopping_cart_hash):
        shopping_cart = None

        if shopping_cart_hash:
            shopping_cart = ShoppingCart.objects.filter(
                hash=shopping_cart_hash
            ).first()

            if shopping_cart is None:
                shopping_cart = self.get_new_shopping_cart()
        else:
            shopping_cart = self.get_new_shopping_cart()

        return shopping_cart

    def dispatch(self, request, *args, **kwargs):
        self.shopping_cart_hash = self.get_shopping_cart_hash(request)
        self.shopping_cart = self.get_shopping_cart(request, self.shopping_cart_hash)

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

    def render_to_response(self, context, **response_kwargs):
        response = super(ShoppingCartMixin, self).render_to_response(
            context, **response_kwargs
        )

        if self.is_new_shopping_cart is True:
            response.set_cookie('shopping_cart', self.shopping_cart.hash)

        return response


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

    def get_shopping_cart_hash(self, request):
        return self.kwargs.get('cart_hash')

    def dispatch(self, request, *args, **kwargs):
        dispatch = super(OrderView, self).dispatch(
            request, *args, **kwargs
        )

        if self.shopping_cart is None:
            return HttpResponseRedirect(reverse('home'))

        return dispatch

    def get_form_kwargs(self):
        kwargs = super(OrderView, self).get_form_kwargs()
        kwargs['shopping_cart'] = self.shopping_cart

        return kwargs
