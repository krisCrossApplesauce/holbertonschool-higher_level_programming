#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) { console.log(err); }
  const filmList = JSON.parse(body).results;
  let count = 0;
  for (const film of filmList) {
    for (const char of film.characters) {
      if (char.includes('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
