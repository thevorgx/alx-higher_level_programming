#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((curr, idx) => curr * idx);
console.log(newList);
