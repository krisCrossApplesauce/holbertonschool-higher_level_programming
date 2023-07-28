#!/usr/bin/node
const process = require('process');
const args = process.argv;
function factorial (a) {
  let n = 1;
  for (let i = 1; i <= a; i++) {
    n = n * i;
  }
  console.log(n);
}
factorial(parseInt(args[2]));
