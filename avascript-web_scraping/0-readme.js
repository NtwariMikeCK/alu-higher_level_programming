#!/usr/bin/node
const fs = require('fs');

// Check if the file path is provided as the first argument
const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: ./0-readme.js <file path>');
  process.exit(1);
}

// Read the file content in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // Print the error object if an error occurs
  } else {
    console.log(data); // Print the file content if no error
  }
});
