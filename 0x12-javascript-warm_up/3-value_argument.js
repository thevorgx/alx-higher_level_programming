#!/usr/bin/node
const args = process.argv;

if (args[2]) {
  for (let i = 2; args[i] !== undefined; i++) {
    console.log(args[i]);
  }
} else {
  console.log('No argument');
}
