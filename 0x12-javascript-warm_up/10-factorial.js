#!/usr/bin/node
/* Write a script that prints factorial of +ve numbers */

const argument = process.argv[2];
const intValue = parseInt(argument);

if (!isNaN(intValue)) {
	if(intValue >= 0){
		console.log(fact(intValue));
	}
}
else{
	console.log(1);
}
function fact(n){
	if (n === 0 || n ===1 ){
		return 1;
	}
else{
	return n * fact(n - 1);
}
}
