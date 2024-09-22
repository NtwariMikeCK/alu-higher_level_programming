#!/usr/bin/node

// Function to compute the factorial recursively
function factorial(n){
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
// Access the first argument passed by the user and convert it to an integer
const num = parseInt(process.argv[2]);

// Print the factorial of the number
console.log(factorial(num));
