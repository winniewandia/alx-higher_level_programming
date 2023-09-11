#!/usr/bin/node
const len = process.argv.length;
const args = process.argv.slice(2).map(Number);
if (len <= 3) {
  console.log(0);
} else {
  let max = args[0];
  for (let i = 1; i < args.length; i++) {
    if (max < args[i]) {
      max = args[i];
    }
  }
  let secondMax = args[0];
  if (secondMax >= max) {
    secondMax = args[1];
  }
  for (let i = 1; i < args.length; i++) {
    if (secondMax < args[i] && args[i] < max) {
      secondMax = args[i];
    }
  }
  console.log(secondMax);
}
