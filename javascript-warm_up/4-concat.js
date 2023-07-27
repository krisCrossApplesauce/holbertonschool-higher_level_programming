#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args[3]) {
  console.log(args[2], ' is ', args[3]);
} else if (args[2]) {
  console.log(args[2], ' is undefined');
} else {
  console.log('undefined is undefined');
}
