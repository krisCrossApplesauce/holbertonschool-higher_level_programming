#!/usr/bin/node
const process = require('process');
const args = process.argv;
function add(a, b) {
  let c = a + b;
  console.log(c);
}
add(parseInt(args[2]), parseInt(args[3]));
