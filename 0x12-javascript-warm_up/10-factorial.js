#!/usr/bin/node
const args = process.argv;

function factorial (num) {
  num = parseInt(num);
  if (num <= 1 || isNaN(num)) {
    return (1);
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(args[2]));
