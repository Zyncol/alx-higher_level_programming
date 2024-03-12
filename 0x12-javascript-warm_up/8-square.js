#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const tx = Number(process.argv[2]);
  let ty = 0;
  while (ty < tx) {
    console.log('X'.repeat(tx));
    ty++;
  }
}
