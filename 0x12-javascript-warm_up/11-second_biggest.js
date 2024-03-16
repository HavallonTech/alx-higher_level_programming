#!/usr/bin/node


const args = process.argv.slice(2);

if(args[0] === undefined){
	console.log(0);
}
else if (args[1] === undefined)
{ 
	console.log(0);
}
else{
	//args.sort(a, b => a - b);
	const newArray = Array.from(new Set(args)).sort((a, b) => b - a);
	console.log(newArray[1]);
	//console.log(args[1]);
}
