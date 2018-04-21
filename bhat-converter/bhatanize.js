window.addEventListener("load", function(){
    var elems =  document.querySelectorAll("body *");
    var func = function(node, rec, writing, abbr){
	if(rec == 0) return;
	Array.prototype.forEach.call(node.childNodes, function(child){
	    if(child.nodeName == "#text"){
		if(writing == "Modern"){
		    child.textContent = Bhat.convert(child.textContent, abbr, true);
		}else{
		    child.textContent = Bhat.convert(child.textContent, abbr, false);
		}
	    }else{
		func(child, rec-1, writing);
	    }
	});
    };

    Array.prototype.forEach.call(elems, function(elem){
	if(elem.getAttribute("data-bhat") != null){
	    var rec = parseInt(elem.getAttribute("data-bhat-rec")) || 1;
	    var writing = elem.getAttribute("data-bhat-writing") || "Traditional"; //Modern or Traditional
	    var abbr = (elem.getAttribute("data-bhat-abbr") != null);

	    console.log(abbr);
	    
	    func(elem, rec, writing, abbr);
	}
    });
});
