#!/usr/bin/node

const process = require('process');
const request = require('request');

const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
