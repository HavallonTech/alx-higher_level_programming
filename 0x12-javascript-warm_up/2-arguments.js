#!/usr/bin/node


const process = require('process');

let args = process.argv;

let totalargs = args.length;
if (totalargs <=  2){
        console.log('No argument');
}
else if (totalargs ===  3){
        console.log('Argument found');
}
else {
	console.log('Arguments found');
}
