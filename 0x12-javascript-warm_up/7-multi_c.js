#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const tx = Number(process.argv[2]);
  let ty = 0;
  while (ty < tx) {
    console.log('C is fun');
    ty++;
  }
}
