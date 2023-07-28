#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length < 2) {
  console.log(0);
}
function secBig (a) {
  let n = 0;
  let big = parseInt(a[2]);
  for (let i = 3; i < a.length; i++) {
    if (parseInt(a[i]) > big) {
      n = big;
      big = parseInt(a[i]);
    } else if (parseInt(a[i]) > n) {
      n = parseInt(a[i]);
    }
  }
  console.log(n);
}
secBig(args);
