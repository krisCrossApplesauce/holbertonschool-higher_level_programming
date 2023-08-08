#!/usr/bin/node
const process = require('process');
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, content) {
  console.log(err || content);
});
