#!/usr/bin/node
/* Write a script that prints My number: <first argument converted in integer> */
/* if the first argument can be converted to an integer */

const argument = process.argv[2];
const intValue = parseInt(argument);
if (!isNaN(intValue) && argument === String(intValue)) {
	const final = 'My number: ' + intValue;
	console.log(final);
}
else{
	console.log('Not a number');
}
