#!/usr/bin/node
const OriginalSquare = require('./5-square');

class Square extends OriginalSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let w = '';
    while (w.length < this.width) {
      w += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(w);
    }
  }
}

module.exports = Square;
