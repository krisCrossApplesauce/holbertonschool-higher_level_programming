#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (parseInt(args[2])) {
  let width = '';
  while (width.length < parseInt(args[2])) {
    width += 'X';
  }
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log(width)
  }
} else {
  console.log('Missing size');
}
