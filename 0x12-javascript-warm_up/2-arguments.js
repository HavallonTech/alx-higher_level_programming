#!/usr/bin/node
/* W script that prints a message depending of the number of arguments passed */

const argv = arguments.length;
if (argv < 1){
console.log('No argument');
}
else if (argv === 1){
console.log('Argument found');
}
else {
console.log('Arguments found');
}
/*
argv.forEach((val, index) =>{
console.log(i${index}: ${val});
});
console.log('C is fun');
console.log('Python is cool');
console.log('JavaScript is amazing'); */
