#!/usr/bin/node

const arg1 = process.argv[2];
const number = Number(arg1);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
};
