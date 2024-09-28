#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  // Instance method to print the square using a custom character 'c'
  charPrinti (c) {
    // If 'c' is undefined, default to 'X'
    const charToPrint = c === undefined ? 'X' : c;

    // Print the square using the given character or 'X'
    for (let i = 0; i < this.height; i++) {
      console.log(charToPrint.repeat(this.width));
    }
  }
}

module.exports = Square;
