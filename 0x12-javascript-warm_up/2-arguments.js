#!/usr/bin/node
/* W script that prints a message depending of the number of arguments passed */

/*const argv = arguments.length; */

const argv = process.argv.length;
if (argv < 1){
console.log('No argument');
}
else if (argv === 1){
console.log('Argument found');
}
else {
console.log('Arguments found');
}
