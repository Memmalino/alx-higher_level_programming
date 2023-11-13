#!/usr/bin/node
const toPrint = `My number: ${Math.floor(process.argv[2])}`;
console.log(Number(process.argv[2]) ? toPrint : 'Not a number');
