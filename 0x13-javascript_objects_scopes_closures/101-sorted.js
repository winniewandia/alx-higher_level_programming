#!/usr/bin/node
const dict = require('./101-data').dict;
const occurencesToUserIDs = {};
for (const userId in dict) {
  if (Object.prototype.hasOwnProperty.call(dict, userId)) {
    const occurrences = dict[userId];
    if (!Object.prototype.hasOwnProperty.call(occurencesToUserIDs, occurrences)) {
      occurencesToUserIDs[occurrences] = [];
    }
    occurencesToUserIDs[occurrences].push(userId);
  }
}
console.log(occurencesToUserIDs);
