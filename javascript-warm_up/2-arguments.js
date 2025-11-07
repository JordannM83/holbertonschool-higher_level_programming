#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] != null) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
