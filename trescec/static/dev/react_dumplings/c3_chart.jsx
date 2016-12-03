import React, {Component} from 'react';
import c3 from 'c3';

class Chart extends Component {
    constructor(props) {
        super(props);
        this.chart = null;
    }

    generateChart() {
        const {data, config, axis, zoom, subchart, padding, tooltip} = this.props;
        const { bindto, ...restConfig } = config;
        const c3Confg = {
            bindto: `#${bindto}`,
            ...restConfig,
            data,
            zoom,
            axis,
            subchart,
            padding,
            tooltip
        };

        if (data.columns && data.columns.length > 0) {
            this.chart = c3.generate(c3Confg);
        } else {
            this.destroyChart();
        }
    }

    destroyChart() {
        if (this.chart) {
            this.chart.destroy();
        }
    }

    componentDidMount() {
        this.generateChart();
    }

    componentDidUpdate(prevProps, prevState) {
        if (this.chart) {
            this.chart.load(this.props.data);
        } else {
            this.generateChart()
        }
    }

    componentWillUnmount() {
        this.destroyChart();
    }

    render() {
        return (
            <div id={this.props.config.bindto}></div>
        );
    }
}

Chart.propTypes = {
    data: React.PropTypes.object,
    config: React.PropTypes.object,
    axis: React.PropTypes.object,
    zoom: React.PropTypes.object,
    subchart: React.PropTypes.object,
    padding: React.PropTypes.object,
    tooltip: React.PropTypes.object
};

Chart.defaultProps = {
    config: {
        bindto: 'chart-id'
    },
    data: {
        columns: []
    }
};

export default Chart;
