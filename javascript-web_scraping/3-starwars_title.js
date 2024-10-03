#!/usr/bin/node
const request = require('request');

// Get the movie ID from the first argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie ID>');
  process.exit(1);
}

// Construct the API URL using the provided movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(url, (err, res, body) => {
  if (err) {
    console.error(err); // Print the error if the request fails
  } else {
    // Parse the response body and extract the title
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
