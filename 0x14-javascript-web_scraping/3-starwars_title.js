#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + id + '/', function (error, response, body) {
  if (error === null) {
    const str = JSON.parse(body);
    console.log(str.title);
  }
});
