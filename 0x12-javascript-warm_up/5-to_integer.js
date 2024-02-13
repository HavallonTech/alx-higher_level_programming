#!/usr/bin/node
/* Write a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer*/

let argument = process.argv[2];
const intValue = parseInt(argument);
if (intValue > 0 ) {
	//const intValue = parseInt(argument);
	let final = 'My number: ' + intValue;
	console.log(final);
}
else{
console.log('Not a number')
}
