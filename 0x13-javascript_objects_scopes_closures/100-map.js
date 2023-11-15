#!/usr/bin/node
const list = require('./100-data.js').list;

const newArray = list.map((name, i) => name * i);
console.log(list);
console.log(newArray);
