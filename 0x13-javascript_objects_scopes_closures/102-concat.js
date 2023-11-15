#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, content) => {
  if (err) {
    console.log('there is an error while reading the file');
  } else {
    fs.readFile(process.argv[3], 'utf-8', (err, content2) => {
      if (err) {
        console.log('there is an error while reading the file');
      } else {
        const printed = `${content}${content2}`;
        fs.writeFile(process.argv[4], printed, err => err);
      }
    });
  }
});
