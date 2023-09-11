#!/usr/bin/node
const len = process.argv.length;
const firstArg = process.argv[2];
if (len === 2 || len === 3) {
  console.log(0);
} else {
  let max = firstArg;
  for (let i = 0; i < len - 2; i++) {
    if (max < process.argv[i + 2]) {
      max = process.argv[i + 2];
    }
  }
  let secondMax = firstArg;
  for (let i = 0; i < len - 2; i++) {
    if (process.argv[i + 2] < process.argv[i + 3] && process.argv[i + 3] < max) {
      secondMax = process.argv[i + 3];
    }
  }
  console.log(secondMax);
}
