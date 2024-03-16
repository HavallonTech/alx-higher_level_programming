#!/usr/bin/node
exports.callMeMoby = function (x, theFunction){
	for (let k = 1; k<=x; k++){
		theFunction();
	}
};
	
