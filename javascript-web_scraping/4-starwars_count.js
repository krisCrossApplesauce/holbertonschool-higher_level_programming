#!/usr/bin/node
const process = require('process');
const url = process.argv[2];
const request = require('request');
const wedgeAntilles = url.substring(0, (url.length - 5)) + 'people/18/';
request(url, function (err, response, body) {
  if (err) { console.log(err); }
  const filmList = JSON.parse(body).results;
  let count = 0;
  for (const film of filmList) {
    for (const char of film.characters) {
      if (char === wedgeAntilles) {
        count += 1;
      }
    }
  }
  console.log(count);
});
