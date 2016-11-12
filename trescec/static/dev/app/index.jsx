import React from 'react';
import {render} from 'react-dom';
import serialize from 'form-serialize';
import hasClass from 'react-kit/hasClass';
import fetchFromServer from '../react_dumplings/fetch_from_server.jsx';

import '../sass/custom.scss';

class App extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
      this.submitForm = this.submitForm.bind(this);
      this.submitProductForm = this.submitProductForm.bind(this);
    }

    componentDidMount () {
        window.addEventListener('submit', this.submitForm);
    }

    submitForm (e) {
        let data = serialize(e.target, { hash: true });
        let isProductForm = hasClass(e.target, 'js-product-form');

        e.preventDefault();

        if (isProductForm) {
            this.submitProductForm(data);
        }
    }

    submitProductForm (data) {
        fetchFromServer.post(API_URL.ORDERITEMS_LIST, data, (data) => {
            console.log(data);
        }, {
            "X-CSRFToken": CSRF_TOKEN
        });
    }

    render () {
        return (<div></div>);
    }
}

render(<App/>, document.getElementById('app'));
