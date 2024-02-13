#!/usr/bin/node
/*script that prints a the first argument passed to it*/

/*const argv = arguments.length;
console.log(argv)*/

const argv = process.argv;

if(argv.lenth < 3){
console.log('No argument');
}
else{
console.log(argv[2]);
}
