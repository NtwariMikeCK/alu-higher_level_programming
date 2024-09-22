#!/usr/bin/node

// Access the first argument (ignoring process.argv[0] and process.argv[1])
const arg = process.argv[2];

// Check if the argument exists and print the appropriate message
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
