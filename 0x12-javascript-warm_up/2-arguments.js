#!/usr/bin/node
/* W script that prints a message depending of the number of arguments passed */

/*const argv = arguments.length;
console.log(argv)*/

const argv = process.argv.length;
if (argv === 3){
console.log('Argument found');
}
else if (argv > 3)
{
console.log('Arguments found');
}
else{
console.log('No argument');
}

