import React from 'react';
import {render} from 'react-dom';

import '../sass/custom.scss';

class App extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    render () {

        return (<div></div>);
    }
}

render(<App/>, document.getElementById('app'));
