#!/usr/bin/node

// Function to add two integers
function add(a, b) {
  return a + b;
}

// Access the first and second arguments passed by the user and convert them to integers
const firstNum = parseInt(process.argv[2]);
const secondNum = parseInt(process.argv[3]);

// Print the result of the addition
console.log(add(firstNum, secondNum));
