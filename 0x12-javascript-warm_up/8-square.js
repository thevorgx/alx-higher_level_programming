#!/usr/bin/node
const args = process.argv;
args[2] = parseInt(args[2]);

if (!isNaN(args[2]) && args.length === 3) {
  for (let i = 0; i < args[2]; i++) {
    let line = '';
    for (let j = 0; j < args[2]; j++) {
      line += 'X ';
    }
    console.log(line);
  }
} else if (isNaN(args[2])) {
  console.log('Missing size');
}
