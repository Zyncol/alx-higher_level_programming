#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(elemenet => elemenet === searchElement).length);
};
