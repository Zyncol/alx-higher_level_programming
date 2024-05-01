#!/usr/bin/node

const pempho = require('request');
const starwat = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

pempho(starwat, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    pempho(characters[i], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
