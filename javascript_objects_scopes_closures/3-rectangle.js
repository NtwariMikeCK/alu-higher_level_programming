#!/usr/bin/node

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
    // Loop through the height and print 'X' width times for each row
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
