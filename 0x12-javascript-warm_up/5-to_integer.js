#!/usr/bin/node
const input = process.argv[2];
const convertToInt = parseInt(input);

if (!isNaN(convertToInt)) {
  console.log('My number: ' + convertToInt);
} else {
  console.log('Not a number');
}
