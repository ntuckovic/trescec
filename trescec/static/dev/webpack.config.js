var webpackConfigTool = require('./react_dumplings/webpack.config');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, '../public');
var APP_DIR = path.resolve(__dirname, 'app');
var SASS_DIR = path.resolve(__dirname, 'sass');

var config = webpackConfigTool({
    dirname: __dirname,
    build_path: BUILD_DIR,
    dev_path: APP_DIR,
    sass_path: SASS_DIR,
    copy_array: [
        { from: 'node_modules/bootstrap/dist', to: 'vendor/bootstrap' },
    ]
});

module.exports = config;
