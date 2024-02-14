#!/usr/bin/node

/** class Rectangle that defines a rectangle: */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let fullWidth = '';
    for (let i = 0; i < this.width; i++) {
      fullWidth += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(fullWidth);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
