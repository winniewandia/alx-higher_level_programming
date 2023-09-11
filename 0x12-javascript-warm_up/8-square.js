#!/usr/bin/node
const input = process.argv[2];
const convertToInt = parseInt(input);
if (isNaN(convertToInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convertToInt; i++) {
    let row = '';
    for (let j = 0; j < convertToInt; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
