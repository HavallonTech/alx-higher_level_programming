#!/usr/bin/node
/* Write a script that prints  square uding x */

let argument = process.argv[2];
const intValue = parseInt(argument);
let i = 1;
let k = 1;
let final = 'X';
if (intValue > 0 ) {
	while (k <= intValue)
	{ 
		while (i <  intValue)
		{
			final = final + 'X';
			i++;
		}
		console.log(final);
		i = 1;
		k++;
		final = 'X';
	}
}
else if(isNaN(argument)){
console.log('Missing size');
}
