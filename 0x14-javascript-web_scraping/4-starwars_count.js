#!/usr/bin/env node
const url = process.argv[2];
const axios = require('axios').default;

// Make a request for a user with a given ID
axios.get(url)
  .then(function (response) {
    let count = 0;
    for (let i = 0; response.data.results[i]; i++) {
      const info = response.data.results[i].characters;
      info.forEach(element => {
        if (element.search('18') !== -1) {
          count++;
        }
      });
    }
    console.log(count);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
