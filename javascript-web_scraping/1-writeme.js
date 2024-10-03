#!/usr/bin/node
const fs = require('fs');

// Get the file path and the string to write from the arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

if (!filePath || !stringToWrite) {
  console.error('Usage: ./1-writeme.js <file path> <string to write>');
  process.exit(1);
}

// Logging the arguments for debugging purposes
console.log(`File path: ${filePath}`);
console.log(`String to write: ${stringToWrite}`);

// Write the string to the file in UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error if writing to the file fails
  }
});
