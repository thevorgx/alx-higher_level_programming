#!/usr/bin/node
const list = require('./100-data').list;
let prev = [0];
const newList = list.map(function (value) {
  const curr = value;
  if (curr < 1) {
    return (curr);
  }
  const res = curr * prev;
  prev = curr;
  return (res);
});
console.log(list);
console.log(newList);
