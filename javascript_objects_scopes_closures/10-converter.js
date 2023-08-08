#!/usr/bin/node
exports.converter = function (base) {
  return function convertNum (num) {
    return (num.toString(base));
  };
};
