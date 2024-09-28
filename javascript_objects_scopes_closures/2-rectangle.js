#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    // Check if w and h are positive integers
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    // If either w or h is 0 or not a positive integer, leave the object empty
  }
}

module.exports = Rectangle;
