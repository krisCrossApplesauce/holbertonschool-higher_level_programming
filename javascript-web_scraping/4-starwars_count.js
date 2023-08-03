#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) { console.log(err); }
  const film_list = JSON.parse(body).results;
  let count = 0;
  for (film of film_list) {
    for (char of film.characters) {
      if ("https://swapi-api.hbtn.io/api/people/18/" === char) {
        count += 1;
      }
    }
  }
  console.log(count);
});
