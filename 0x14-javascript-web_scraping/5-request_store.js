#!/usr/bin/node

const pempho = require('request');
const tx = require('fs');

pempho(process.argv[2], function (_err, _res, body) {
  tx.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
