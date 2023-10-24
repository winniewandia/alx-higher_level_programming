#!/usr/bin/node
const request = require('request');
const responseDict = {};
request(process.argv[2], function (error, response, body) {
  if (error === null) {
    const str = JSON.parse(body);
    for (let i = 0; i < str.length; i++) {
      if (str[i].completed === true) {
        if (responseDict[str[i].userId] === undefined) {
          responseDict[str[i].userId] = 0;
        }
        responseDict[str[i].userId]++;
      }
    }
    console.log(responseDict);
  }
});
