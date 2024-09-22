#!/usr/bin/node

// Access the first argument passed by the user and convert it to an integer
const x = parseInt(process.argv[2]);

// Check if the argument is a valid integer
if (isNaN(x)) {
  console.log('Missing size');
} else {
  // Use a loop to print 'C is fun' x times
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
