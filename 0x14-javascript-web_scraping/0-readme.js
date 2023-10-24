#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, body) {
  if (body === undefined) {
    console.log(error);
  } else {
    console.log(body);
  }
});
