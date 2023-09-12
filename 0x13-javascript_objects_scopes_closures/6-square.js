#!/usr/bin/node
const _Square = require('./5-square');
class Square extends _Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let char = '';
      for (let j = 0; j < this.width; j++) {
        char += c;
      }
      console.log(char);
    }
  }
}
module.exports = Square;
