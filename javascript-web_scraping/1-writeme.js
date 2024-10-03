#!/usr/bin/node
const fs = require('fs');

// Check if the file path and string to write are provided as arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

if (!filePath || !stringToWrite) {
  console.error('Usage: ./1-writeme.js <file path> "<string to write>"');
  process.exit(1);
}

// Write the string to the file in utf-8
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error object if an error occurs
  }
});
