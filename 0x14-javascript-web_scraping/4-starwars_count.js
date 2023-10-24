#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (error === null) {
    const str = JSON.parse(body);
    const result = str.results;
    for (let i = 0; i < result.length; i++) {
      const character = result[i].characters;
      for (let j = 0; j < character.length; j++) {
        if (character[j].search('18') > 0) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
