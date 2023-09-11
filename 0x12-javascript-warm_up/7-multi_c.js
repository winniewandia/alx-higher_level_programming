#!/usr/bin/node
const input = process.argv[2];
const convertToInt = parseInt(input);

if (isNaN(convertToInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convertToInt; i++) {
    console.log('C is fun');
  }
}
