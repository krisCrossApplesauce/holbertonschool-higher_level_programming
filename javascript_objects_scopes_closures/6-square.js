#!/usr/bin/node
const OriginalSquare = require('./5-square');

class Square extends OriginalSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let width = '';
    while (width.length < this.size) {
      if (c) {
        width += c;
      } else {
        width += 'X';
      }
    }
    for (let i = 0; i < this.size; i++) {
      console.log(width);
    }
  }
}

module.exports = Square;
