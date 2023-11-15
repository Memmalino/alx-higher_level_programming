#!/usr/bin/node
const dict = require('./101-data.js').dict;
const arr = {};
for (const k in dict) {
  if (!arr[dict[k]]) {
    arr[dict[k]] = [parseInt(k)];
  } else {
    arr[dict[k]].push(parseInt(k));
  }
}
console.log(arr);
