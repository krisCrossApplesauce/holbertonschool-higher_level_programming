#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length < 2) {
  console.log(0);
}
function sec_big (a) {
  let n = 0;
  let big = a[2];
  for (let i = 3; i < a.length; i++) {
    if (a[i] > big) {
      n = big;
      big = a[i];
    } else if (a[i] > n) {
      n = a[i];
    }
  }
  console.log(n);
}
sec_big(args);
