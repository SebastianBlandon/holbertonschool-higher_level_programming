#!/usr/bin/node
const fs = require('fs');
const axios = require('axios').default;
const url = process.argv[2];
axios.get(url)
  .then(function (response) {
    try {
      fs.writeFileSync(process.argv[3], response.data, { encoding: 'utf-8', flag: 'w+' });
    } catch (err) {
      console.log(err);
    }
  });
