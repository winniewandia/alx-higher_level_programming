#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const val1 = process.argv[2];
const value1 = parseInt(val1);
const val2 = process.argv[3];
const value2 = parseInt(val2);
console.log(add(value1, value2));
