#!/usr/bin/node
function factorial (n) {
  if (n === 1 || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const input = process.argv[2];
const val = parseInt(input);
if (isNaN(val)) {
  console.log(1);
} else {
  console.log(factorial(val));
}
