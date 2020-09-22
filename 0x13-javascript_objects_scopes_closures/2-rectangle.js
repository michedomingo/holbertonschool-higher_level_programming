#!/usr/bin/node

class Rectangle {
  constructor (w, h) {

    if (parseInt(h) > 0 && parseInt(w) > 0) {
      this.height = h;
      this.width = w;
    }
  }
}

module.exports = Rectangle;
