#!/usr/bin/node


const args = process.argv.slice(2);

function fact(num){
	if (num === 0 || isNaN(num)) {
    		return (1);
  	} 
else {
	return (fact(num - 1) * num);
}
	
}
console.log(fact(args[0]));
