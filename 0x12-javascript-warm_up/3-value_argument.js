#!/usr/bin/node
/*script that prints a the first argument passed to it*/

/*const argv = arguments.length;
console.log(argv)*/

const argv = process.argv;

if (argv.length >= 3)
{
console.log(argv[2]);
}
