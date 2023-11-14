#!/usr/bin/node
let num = 0; let flag = 0;
if (process.argv.length < 3 || process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > num) {
      num = parseInt(process.argv[i]);
    }
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > flag && parseInt(process.argv[i]) < num) {
      flag = parseInt(process.argv[i]);
    }
  }
  console.log(flag);
}
