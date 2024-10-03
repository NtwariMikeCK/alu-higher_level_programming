#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  // Loop through the list and count occurrences of searchElement
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
