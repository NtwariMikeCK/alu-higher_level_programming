#!/usr/bin/node
const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API URL>');
  process.exit(1);
}

// Make a GET request to the API URL
request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err); // Print the error if the request fails
  } else {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    // Loop through each task and count completed tasks by user ID
    tasks.forEach((task) => {
      if (task.completed) {
        if (!completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId] = 0;
        }
        completedTasksByUser[task.userId]++;
      }
    });

    // Print the result: users with their completed tasks count
    console.log(completedTasksByUser);
  }
});
