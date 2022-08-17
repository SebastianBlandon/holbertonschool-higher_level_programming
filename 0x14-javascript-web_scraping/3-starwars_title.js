#!/usr/bin/node
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id + '/';
const axios = require('axios').default;

// Make a request for a user with a given ID
axios.get(url)
  .then(function (response) {
    // handle success
    console.log(response.data.title);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
