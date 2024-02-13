#!/usr/bin/node
/* Write a script that prints x times “C is fun”*/

let argument = process.argv[2];
const intValue = parseInt(argument);
let i = 1;
if (intValue > 0 ) {
	while (i <=  intValue)
	{
		console.log('C is fun');
		i++;
	}
}
else{
console.log('Missing number of occurrences')
}
