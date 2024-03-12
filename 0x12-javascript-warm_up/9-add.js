#!/usr/bin/node
function add (a, b) {
  const sUm = a + b;
  console.log(sUm);
}

add(Number(process.argv[2]), Number(process.argv[3]));
