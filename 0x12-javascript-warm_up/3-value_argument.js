#!/usr/bin/node
/*	script that prints a the first argument passed to it */

const argv = process.argv[2];

if(typeof argv === 'undefined'){
console.log('No argument');
}
else{
console.log(argv);
}
