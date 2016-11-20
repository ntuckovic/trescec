import React from 'react';
import {render} from 'react-dom';
import serialize from 'form-serialize';
import hasClass from 'react-kit/hasClass';
import fetchFromServer from '../react_dumplings/fetch_from_server.jsx';
import * as Cookies from "js-cookie";
import $ from "jquery";

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

    submitProductForm (data) {
        const existingShoppingCart = Cookies.get('shopping_cart');
        data.shopping_cart = existingShoppingCart || false;

        fetchFromServer.post(API_URL.ORDERITEMS_LIST, data, (data) => {
            if (!existingShoppingCart) {
                Cookies.set('shopping_cart', data.shopping_cart.hash);
            }
        }, {
            "X-CSRFToken": CSRF_TOKEN
        });
    }

    updateOrderItem (e) {
        let data, id;

        e.preventDefault();

        console.log($(e.target));
        // data = serialize(formEl, { hash: true });
        // id = formEl.getAttribute('data-order-item-id');
        // this.submitOrderItemForm(data, id);
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
        let selector = `.price[data-order-item-id="${data.id}"] .calculated-price`;
        let orderItemPriceSpan = document.querySelector(selector);

        orderItemPriceSpan.innerHTML = data.calculated_price;
    }

    deleteOrderItemClicked (e) {
        let id;

        e.preventDefault();

        console.log("drek");
    }

    render () {
        return (<div></div>);
    }
}

render(<App/>, document.getElementById('app'));
