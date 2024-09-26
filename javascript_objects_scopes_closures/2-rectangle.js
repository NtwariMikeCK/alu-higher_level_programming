#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    // Check if w and h are positive integers and non-zero
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if conditions are not met
      return {};
    }
  }
}

module.exports = Rectangle;
