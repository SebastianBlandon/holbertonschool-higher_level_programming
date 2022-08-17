#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios').default;

// Make a request for a user with a given ID
axios.get(url)
  .then(function (response) {
    // handle success
    console.log('code:', response.status);
  })
  .catch(function (error) {
    // handle error
    console.log('code: 404');
  })
  .then(function () {
    // always executed
  });
