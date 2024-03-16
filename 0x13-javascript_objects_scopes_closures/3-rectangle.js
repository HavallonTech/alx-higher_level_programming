#!/usr/bin/node
class Rectangle{
	constructor(w, h) {
		if (parseInt(w) > 0 && parseInt(h) > 0){
			this.width = w;
			this.height = h;
			}
	}
print(){
	let i = this.width;
	let imgSym = ""
	while (i >= 1){
		imgSym += "X";
		i--;
	}
	while ( this.height >= 1){
		console.log(imgSym);
		this.height--;
	}
	
}
}
module.exports = Rectangle;
