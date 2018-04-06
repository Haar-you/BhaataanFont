window.addEventListener("load", function(){
    var div = document.getElementById("bhaataan");
    var text = "";

    text += "<div>";
    for(var c=0xe000; c<=0xe01d; ++c){	
	text += String.fromCharCode(c);
    }
    text += "</div>";
    
    for(var v=0xe020; v<=0xe029; ++v){
	text += "<div>";
	for(var c=0xe000; c<=0xe01d; ++c){	
	    text += String.fromCharCode(c,v);
	}
	text += "</div>";
    }

    for(var v=0xe020; v<=0xe028; ++v){
	text += "<div>";
	for(var c=0xe000; c<=0xe01d; ++c){	
	    text += String.fromCharCode(c,v,0xe029);
	}
	text += "</div>";
    }
    text += "<div>";
    for(var c=0xe000; c<=0xe01d; ++c){	
	text += String.fromCharCode(c,0xe02f);
    }
    text += "</div>";
    

    text += "<div>";
    for(var v=0xe020; v<=0xe029; ++v){
	text += String.fromCharCode(v);
    }
    text += "</div>";
    
    for(var c=0xe000; c<=0xe01d; ++c){
    	text += "<div>";
	for(var v=0xe020; v<=0xe029; ++v){
	    text += String.fromCharCode(c,v);
	}
	text += String.fromCharCode(c,0xe02f);
	for(var v=0xe020; v<=0xe028; ++v){
	    text += String.fromCharCode(c,v,0xe029);
	}
	text += "</div>";
    }

    text += "<div>";
    for(var p=0xe02a; p<=0xe02e; ++p){
	text += String.fromCharCode(p);
    }
    text += "</div>";
    
    

    div.innerHTML = text;

});

