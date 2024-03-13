#!/usr/bin/node


const process = require('process');

let argsv = process.argv.slice(2);
if(argsv[0] === undefined){
console.log('No argument');
}
else {
console.log(argsv[0]);
}
