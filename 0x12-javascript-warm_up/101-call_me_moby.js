#!/usr/bin/node
export.callMeMoby = function (x, theFunction){
	for (let k = 1; k<=x; k++){
		theFunction();
	}
};
	
