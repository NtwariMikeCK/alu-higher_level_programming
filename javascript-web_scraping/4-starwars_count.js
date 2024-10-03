#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const films = JSON.parse(body).results;
  let count = 0;

  // Count the number of films featuring Wedge Antilles
  films.forEach((film) => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
      count++;
    }
  });

  // Print the count of movies
  console.log(count);
});
