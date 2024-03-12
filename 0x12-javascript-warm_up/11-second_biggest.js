#!/usr/bin/node
const args = process.argv.slice(2);
function secondBig (array) {
  let biggest = array[0];
  let secBiggest = -Infinity;
  if (array.length <= 1) {
    return (0);
  }
  for (let i = 1; i < array.length; i++) {
    if (array[i] > biggest) {
      secBiggest = biggest;
      biggest = array[i];
    } else if (array[i] < biggest && array[i] > secBiggest) {
      secBiggest = array[i];
    }
  }
  return secBiggest;
}
console.log(secondBig(args));
