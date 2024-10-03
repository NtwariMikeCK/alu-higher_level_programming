#!/usr/bin/node
const fs = require('fs');

// Get the file path and the string to write from the arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Check if the file path or string is missing
if (!filePath || stringToWrite === undefined) {
  console.error('(0 chars long)\n[stderr]: [Anything]\n(0 chars long)');
  process.exit(1);
}

// If the string is provided, write the string to the file in UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error if writing to the file fails
  }
});
