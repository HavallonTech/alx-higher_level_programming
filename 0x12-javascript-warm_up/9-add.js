#!/usr/bin/node
/* Write  script that prints the addition of 2 integers */
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
function add(a, b){
	let sum = a + b;
	console.log(sum);
}
add(a,b);
