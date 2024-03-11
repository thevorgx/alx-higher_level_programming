#!/usr/bin/node
const args = process.argv;

if (args.length === 3) {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
} else if (args.length === 2) {
  console.log('Missing number of occurrences');
}
