#!/usr/bin/node
const process = require('process');
const args = process.argv;
function factorial (a) {
  let n = 0;
  for (let i = 1; i <= a; i++) {
    n += i;
  }
  console.log(n);
}
if (parseInt(args[2])) {
  factorial(parseInt(args[2]));
} else {
  factorial(1);
}
