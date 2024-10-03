#!/usr/bin/node
const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

// Character ID for Wedge Antilles
const wedgeAntillesId = '18';

// Make a GET request to the provided API URL (films endpoint)
request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err); // Print the error if the request fails
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    // Loop through each film and check if Wedge Antilles is in the character list
    for (const film of films) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    }

    // Print the number of films where Wedge Antilles is present
    console.log(count);
  }
});
