#!/usr/bin/node

exports.converter = function (base) {
  return function (ntb) {
    return ntb.toString(base);
  };
};
