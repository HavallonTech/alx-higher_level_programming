#!/usr/bin/node
const data_read = require('fs');
const File_name = process.argv[2];
data_read.readFile(File_name, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
