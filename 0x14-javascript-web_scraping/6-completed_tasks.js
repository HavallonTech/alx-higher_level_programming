#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const i in tasks) {
      if (tasks[i].completed === true) {
        if (completed[tasks[i].userId] === undefined) {
          completed[tasks[i].userId] = 1;
        } else {
          completed[tasks[i].userId] += 1;
        }
      }
    }
    console.log(completed);
  }
});
