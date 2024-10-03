#!/usr/bin/node
const request = require('request');

// Get the URL from the first argument
const url = process.argv[2];

if (!url) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Make a GET request to the specified URL
request(url, (err, res) => {
  if (err) {
    console.error(err); // Print the error if the request fails
  } else {
    // Print the status code of the response
    console.log(`code: ${res.statusCode}`);
  }
});
