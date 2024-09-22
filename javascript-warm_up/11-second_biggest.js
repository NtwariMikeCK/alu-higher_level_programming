#!/usr/bin/node

// Check if the number of arguments passed is less than 2
if (process.argv.length <= 3) {
  console.log(0);
} else {
  // Convert arguments to integers and sort them in descending order
  const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);
  // Print the second largest integer (which is the second element in the sorted array)
  console.log(args[1]);
}
