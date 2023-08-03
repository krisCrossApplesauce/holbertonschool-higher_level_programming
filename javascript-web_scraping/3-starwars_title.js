#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.log(err); }
  const filmObj = JSON.parse(body);
  console.log(filmObj.title);
});
