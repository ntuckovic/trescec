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
      this.submitProductForm = this.submitProductForm.bind(this);
      this.inputChanged = this.inputChanged.bind(this);
      this.submitOrderItemForm = this.submitOrderItemForm.bind(this);
    }

    componentDidMount () {
        window.addEventListener('submit', this.submitForm);
        window.addEventListener('change', this.inputChanged);
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

    inputChanged (e) {
        const formEl = e.target.form;
        let isOrderItemForm = hasClass(formEl, 'js-order-item-form');
        let data, id;

        if (isOrderItemForm) {
            e.preventDefault();
            data = serialize(formEl, { hash: true });
            id = formEl.getAttribute('data-order-item-id');
            this.submitOrderItemForm(data, id);
        }
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

    render () {
        return (<div></div>);
    }
}

render(<App/>, document.getElementById('app'));
