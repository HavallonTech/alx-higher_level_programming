#!/usr/bin/node


const args = process.argv.slice(2);

let x = args[0];
let output = '';
if (parseInt(args[0])){
	let y = x;
	let temp = x;
	while (x > 0){
		y = temp;
		while (y > 0){
			output = output + 'X';
			y--;
		}
		console.log(output);
		output = '';
		x--;
	}
}
else{
	console.log('Missing size');
	}
	
