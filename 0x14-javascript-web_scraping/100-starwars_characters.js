#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + id, function (error, response, body) {
  if (error === null) {
    const str = JSON.parse(body);
    const characters = str.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, body) {
        if (error === null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
