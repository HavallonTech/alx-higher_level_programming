#!/usr/bin/node

/** class Rectangle that defines a square: */

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let container = '';
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
        container += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(container);
      }
    } else {
      for (let k = 0; k < this.width; k++) {
        container += 'X';
      }
      for (let l = 0; l < this.height; l++) {
        console.log(container);
      }
    }
  }
}

module.exports = Square;
