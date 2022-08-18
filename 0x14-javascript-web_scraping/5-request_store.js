#!/usr/bin/node
const fs = require('fs');
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    try {
      fs.writeFileSync(process.argv[3], response.data, { encoding: 'utf-8', flag: 'w+' });
    } catch (err) {
      console.log(err);
    }
  });
