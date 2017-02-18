/*
Example usage:
==============
import fetchFromServer from 'react-dumplings/fetch_from_server.jsx';

fetchFromServer.fetch("http://my-api-link.exmpla", (data) => {
    console.log(data);
    console.log('jaaj!');
});
*/

import NProgress from 'react-nprogress';




const fetchFromServer = {
    checkStatus: (response) => {
        let returnObj = {
            response: response,
            success: false
        };

        if (response.status >= 200 && response.status < 300) {
            returnObj.success = true
        }

        return returnObj
    },

    parseJSON: (result) => {
        let returnObj = {
            success: result.success
        }

        if (result.success) {
            returnObj.data = result.response.json()
        } else {
            returnObj.data = result.response
        }

        return returnObj
    },

    mergeHeaders: (headers={}) => {
        const defaultHeaders = {
            'Content-Type': 'application/json'
        };

        headers = Object.assign(headers, defaultHeaders)

        return headers;
    },

    handleResult: (onSuccess, onFail, result) => {
        if (result.success) {
            if (result.data) {
                result.data.then((data) => {
                    onSuccess(data)
                })
            } else {
                onSuccess()
            }
        } else {
            if (onFail) {
                if (result.data) {
                    result.data.json().then((data) => {
                        onFail(data)
                    })
                } else {
                    onFail()
                }
            } else {
                throw new Error(result.data.statusText)
            }
        }
    },

    fetch: (opts) => {
        NProgress.start();

        return fetch(opts.url, {
              credentials: 'same-origin'
            })
            .then(fetchFromServer.checkStatus)
            .then(fetchFromServer.parseJSON)
            .then((result) => {
                fetchFromServer.handleResult(opts.onSuccess, opts.onFail, result)

                NProgress.done();
            })
    },

    post: (opts) => {
        NProgress.start();

        opts.method = opts.method || 'POST'
        opts.headers = opts.headers || {}

        return fetch(opts.url, {
              credentials: 'same-origin',
              method: opts.method,
              headers: fetchFromServer.mergeHeaders(opts.headers),
              body: JSON.stringify(opts.data)
            })
            .then(fetchFromServer.checkStatus)
            .then(fetchFromServer.parseJSON)
            .then((result) => {
                fetchFromServer.handleResult(opts.onSuccess, opts.onFail, result)

                NProgress.done()
            })
    },

    put: (opts) => {
        opts.method = 'PUT'

        return fetchFromServer.post(opts);
    },

    delete: (opts) => {
        NProgress.start();

        return fetch(opts.url, {
          credentials: 'same-origin',
          method: 'DELETE',
          headers: fetchFromServer.mergeHeaders(opts.headers)
        })
        .then(fetchFromServer.checkStatus)
        .then((result) => {
            fetchFromServer.handleResult(opts.onSuccess, opts.onFail, result)

            NProgress.done()
        });
    },
};

module.exports = fetchFromServer;
