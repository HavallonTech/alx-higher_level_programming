#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const result = JSON.parse(body);
    console.log(result.title);
  }
});
