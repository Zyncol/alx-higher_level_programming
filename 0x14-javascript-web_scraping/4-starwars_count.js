#!/usr/bin/node

const pempho = require('request');
const starwat = process.argv[2];
let nthawi = 0;

pempho(starwat, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let k = 0; k < body.length; ++k) {
    const characters = body[k].characters;

    for (let l = 0; l < characters.length; ++l) {
      const character = characters[l];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        nthawi += 1;
      }
    }
  }

  console.log(nthawi);
});
