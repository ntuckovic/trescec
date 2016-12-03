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
        if (response.status >= 200 && response.status < 300) {
            return response
        } else {
            let error = new Error(response.statusText)
            error.response = response
            throw error
        }
    },

    parseJSON: (response) => {
        return response.json()
    },

    mergeHeaders: (headers={}) => {
        const defaultHeaders = {
            'Content-Type': 'application/json'
        };

        headers = Object.assign(headers, defaultHeaders)

        return headers;
    },

    fetch: (url, onSuccess) => {
        NProgress.start();

        return fetch(url, {
              credentials: 'same-origin'
            })
            .then(fetchFromServer.checkStatus)
            .then(fetchFromServer.parseJSON)
            .then(function(data) {
                onSuccess(data);

                NProgress.done();
            })
    },

    post: (url, data, onSuccess, headers={}, method='POST') => {
        NProgress.start();

        return fetch(url, {
              credentials: 'same-origin',
              method: method,
              headers: fetchFromServer.mergeHeaders(headers),
              body: JSON.stringify(data)
            })
            .then(fetchFromServer.checkStatus)
            .then(fetchFromServer.parseJSON)
            .then(function(data) {
                onSuccess(data);
                NProgress.done();
            })
    },

    put: (url, data, onSuccess, headers={}) => {
        return fetchFromServer.post(url, data, onSuccess, headers, 'PUT');
    },

    delete: (url, onSuccess, headers={}) => {

        return fetch(url, {
          credentials: 'same-origin',
          method: 'DELETE',
          headers: fetchFromServer.mergeHeaders(headers)
        })
        .then(fetchFromServer.checkStatus)
        .then(function(data) {
            onSuccess(data);
            NProgress.done();
        });
    },
};

module.exports = fetchFromServer;
