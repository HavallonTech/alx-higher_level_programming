#!/usr/bin/node

let argsv = process.argv.slice(2);

if (Number(argsv[0])){
	console.log('My number: ' + argsv[0]);
}
else{
	console.log('Not a number');
}
