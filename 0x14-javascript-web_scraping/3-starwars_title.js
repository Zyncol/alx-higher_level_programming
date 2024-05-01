#!/usr/bin/node

const pempho = require('request');
const starwat = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

pempho(starwat, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
