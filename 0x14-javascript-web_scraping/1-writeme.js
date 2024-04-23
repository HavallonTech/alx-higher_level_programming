#!/usr/bin/node
const fs = require('fs');
const Filename = process.argv[2];
const contentToAdd = process.argv[3];
fs.appendFile(Filename, contentToAdd, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
