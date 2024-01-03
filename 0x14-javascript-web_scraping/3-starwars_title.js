#!/usr/bin/node

const process = require('process');
const request = require('request');

const episode = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;
let data;

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    console.log(data.title);
  }
});
