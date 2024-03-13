#!/usr/bin/node
exports.esrever = function (list) {
  const j = [];
  for (let k = list.length - 1; k >= 0; k--) {
    j.push(list[k]);
  }
  return (j);
};
