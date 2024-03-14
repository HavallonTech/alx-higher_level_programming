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
	let biggest = process.argv[2];
	for(let i = 2; i < process.argv.length; i++) {
 		if (biggest < Number(process.argv[i])){
			biggest = process.argv[i];
		}
	}
	let biggest2 = process.argv[2];
          for(let i = 2; i < process.argv.length; i++) {
                  if (Number(process.argv[i]) >> biggest2 && (biggest < biggest2)){
                          biggest2 = process.argv[i];
                  }
          }
	console.log(biggest2);
}
