#!/usr/bin/node


const args = process.argv.slice(2);

let x = args[0];
if (parseInt(args[0])){
	while (x > 0){
		console.log('C is fun');
		x--;
	}
}
else{
	console.log('Missing number of occurrences');
	}
	
