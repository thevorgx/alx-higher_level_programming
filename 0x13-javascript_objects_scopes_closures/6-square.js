#!/usr/bin/node
const SquareCode = require('./5-square');
module.exports = class Square extends SquareCode {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
};
