import React from 'react';
import {render} from 'react-dom';
import serialize from 'form-serialize';
import hasClass from 'react-kit/hasClass';

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
        let isProductForm = hasClass(e.target, 'js-product-form');
        let serialized = serialize(e.target, { hash: true });

        e.preventDefault();

        if (isProductForm) {
            this.submitProductForm(serialized);
        }
    }

    submitProductForm (data) {
        console.log(data);
    }

    render () {
        return (<div></div>);
    }
}

render(<App/>, document.getElementById('app'));
