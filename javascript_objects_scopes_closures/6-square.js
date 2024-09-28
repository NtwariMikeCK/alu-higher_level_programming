#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    // If the character 'c' is not passed, default to 'X'
    if (c === undefined) {
      c = 'X';
    }
    // Print the square using the character 'c'
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
