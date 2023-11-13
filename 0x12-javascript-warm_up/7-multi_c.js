#!/usr/bin/node
const firstArg = Number(process.argv[2]);
if (Number.isInteger(firstArg)) {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
