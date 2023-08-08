#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let w = '';
    while (w.length < this.width) {
      w += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(w);
    }
  }

  rotate () {
    const newH = this.width;
    const newW = this.height;
    this.width = newW;
    this.height = newH;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
