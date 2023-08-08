#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (parseInt(args[2])) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
