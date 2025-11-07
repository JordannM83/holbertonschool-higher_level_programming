#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] == null) {
  console.log('No argument');
} else {
  const args = process.argv.slice(2);
  args.forEach(value => {
    console.log(value);
  });
}
