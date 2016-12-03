var webpack = require('webpack');
var path = require('path');
var CopyWebpackPlugin = require('copy-webpack-plugin');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

/*
Usage:

var webpack_config_tool = require('./webpack_config_tool/webpack.config');

var config = webpack_config_tool({
    build_path: 'src/client/public',
    dev_path: 'src/client/dev/app',
    sass_path: 'src/client/dev/sass',
    entry; 'index.jsx',
    filename: 'bundle.js',
    copy_array: [
        { from: 'node_modules/bootstrap/dist', to: 'vendor/bootstrap' },
        { from: 'node_modules/c3/c3.min.css', to: 'vendor/c3/c3.min.css' },
    ]
});

module.exports = config;
*/
var webpackConfigTool = function (opts) {
    opts.build_path = opts.build_path || 'src/client/public';
    opts.dev_path = opts.dev_path || 'src/client/dev/app';
    opts.sass_path = opts.sass_path || 'src/client/dev/sass';
    opts.entry = opts.entry || 'index.jsx';
    opts.filename = opts.filename || 'bundle.js';
    opts.copy_array = opts.copy_array || [];
    opts.react_dumplings_path = opts.react_dumplings_path || path.resolve(opts.dirname, 'react_dumplings');
    opts.include_babel_paths = opts.include_babel_paths || [opts.dev_path, opts.react_dumplings_path];

    var config = {
        entry: ['whatwg-fetch', opts.dev_path + '/' + opts.entry ],
        output: {
            path: opts.build_path,
            filename: opts.filename
        },

        module: {
            loaders: [
            {
                test: /\.jsx?/,
                include: opts.include_babel_paths,
                loader: 'babel',
                query: {
                  presets: ['es2015', 'stage-0', 'react']
                }

            },
            {
                test: /\.scss$/,
                include: opts.sass_path,
                loader: ExtractTextPlugin.extract(
                    'style', // The backup style loader
                    'css?sourceMap!sass?sourceMap'
                )
            }]
        },

        plugins: [
            new CopyWebpackPlugin(opts.copy_array),
            new ExtractTextPlugin('css/style.css')
        ]
    };

    return config;
};

module.exports = webpackConfigTool;
