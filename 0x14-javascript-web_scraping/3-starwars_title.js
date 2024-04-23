#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i in results) {
      const characters = results[i].characters;
      for (const j in characters) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
