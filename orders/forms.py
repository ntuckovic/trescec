# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms import ModelForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .models import Order


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

    def send_email(self, shopping_cart, order_items, order):
        msg_txt = render_to_string(
            'orders/order_email_message.txt',
            {
                'shopping_cart': shopping_cart,
                'order_items': order_items,
                'order': order
            }
        )
        # msg_html = render_to_string(
        #     'orders/order_email_message.html',
        #     {
        #         'shopping_cart': shopping_cart,
        #         'order_items': order_items,
        #         'order': order
        #     }
        # )

        email = send_mail(
            subject=_('Order No. {0}').format(order.id),
            from_email=settings.SHOP_SYSTEM_EMAIL,
            recipient_list=settings.SHOP_ADMIN_EMAILS,
            message=msg_txt,
            # html_message=msg_html,
        )

        return email

    def save(self, force_insert=False, force_update=False, commit=True):
        order = super(OrderForm, self).save(commit=False)
        order_items = self.shopping_cart.get_items()

        order.status = 'OR'
        order.finished_on = timezone.now()

        order.save()
        order_items.update(
            order=order
        )

        self.shopping_cart.ordered = True
        self.shopping_cart.save()

        self.send_email(
            shopping_cart=self.shopping_cart,
            order_items=order_items,
            order=order
        )

        return order
