import React from 'react';
import {render} from 'react-dom';
import serialize from 'form-serialize';
import hasClass from 'react-kit/hasClass';
import fetchFromServer from '../react_dumplings/fetch_from_server.jsx';
import * as Cookies from "js-cookie";

import '../sass/custom.scss';

class App extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
      this.submitForm = this.submitForm.bind(this);
      this.updateOrderItem = this.updateOrderItem.bind(this);
      this.deleteOrderItemClicked = this.deleteOrderItemClicked.bind(this);

      this.submitProductForm = this.submitProductForm.bind(this);
      this.submitOrderItemForm = this.submitOrderItemForm.bind(this);
    }

    componentDidMount () {
        window.addEventListener('submit', this.submitForm);
        $(".js-update-item").on('change', this.updateOrderItem);
        $('.js-delete-order-item').on('click', this.deleteOrderItemClicked);
    }

    componentWillUnmount () {
        window.removeEventListener('submit', this.submitForm);
        $(".js-update-item").off('change');
        $('.js-delete-order-item').off('click');
    }

    submitForm (e) {
        let data = serialize(e.target, { hash: true });
        let isProductForm = hasClass(e.target, 'js-product-form');
        let isOrderItemForm = hasClass(e.target, 'js-order-item-form');

        if (isProductForm) {
            e.preventDefault();
            this.submitProductForm(data);
        }

        if (isOrderItemForm) {
            e.preventDefault();
        }
    }

    updateShoppingCartItemsCount (count) {
        Cookies.set('shopping_cart_items_count', count);
        $('.js-shopping-cart-badge').html(count);
    }

    decreaseShoppingCartItemsCount () {
        let currentCount = Cookies.get('shopping_cart_items_count', 0);
        let newCount = currentCount - 1;

        this.updateShoppingCartItemsCount(newCount);
    }

    submitProductForm (data) {
        const existingShoppingCart = Cookies.get('shopping_cart');
        data.shopping_cart = existingShoppingCart || false;

        fetchFromServer.post(API_URL.ORDERITEMS_LIST, data, (data) => {
            Cookies.set('shopping_cart', data.shopping_cart.hash);
            this.updateShoppingCartItemsCount(data.shopping_cart.items_count)
        }, {
            "X-CSRFToken": CSRF_TOKEN
        });
    }

    updateOrderItem (e) {
        let $form = $(e.target).parent('form');
        let data = serialize($form[0], { hash: true });
        let id = $form.data('order-item-id');

        e.preventDefault();

        this.submitOrderItemForm(data, id);
    }

    submitOrderItemForm (data, id) {
        const orderItemUrl = `${API_URL.ORDERITEMS_LIST}${id}/`;

        fetchFromServer.put(orderItemUrl, data, (data) => {
            this.updateItemTotalPrice(data);
        }, {
            "X-CSRFToken": CSRF_TOKEN
        });
    }

    updateItemTotalPrice (data) {
        const selector = `.price[data-order-item-id="${data.id}"] .calculated-price`;
        const orderItemPriceSpan = document.querySelector(selector);

        orderItemPriceSpan.innerHTML = data.calculated_price;
    }

    deleteOrderItemClicked (e, elem) {
        let $orderItemTr = $(e.currentTarget).parents(".order-item-tr");
        let id = $(e.currentTarget).data('order-item-id');
        let orderItemUrl = `${API_URL.ORDERITEMS_LIST}${id}/`;

        e.preventDefault();

        fetchFromServer.delete(orderItemUrl, (data) => {
            $orderItemTr.remove()
            this.decreaseShoppingCartItemsCount()
        }, {
            "X-CSRFToken": CSRF_TOKEN
        });
    }

    render () {
        return (<div></div>);
    }
}

render(<App/>, document.getElementById('app'));
