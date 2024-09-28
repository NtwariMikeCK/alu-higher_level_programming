#!/usr/bin/node
// 4-rectangle.js
class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers and non-zero
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if conditions are not met
      return {};
    }
  }

  // Instance method to print the rectangle using 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Instance method to exchange the width and height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Instance method to double the width and height of the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
