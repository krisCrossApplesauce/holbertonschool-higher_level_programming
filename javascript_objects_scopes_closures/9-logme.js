#!/usr/bin/node
let num = 0;
exports.logMe = function (item) {
  const text = num + ':';
  console.log(text, item);
  num += 1;
};
