var handler = {
    get : function(target, name){
	return name in target ? target[name] : name;
    }
};

var map = new Proxy({
    "noC": String.fromCharCode(0xe000),
    "t": String.fromCharCode(0xe001),
    "k": String.fromCharCode(0xe002),
    "x": String.fromCharCode(0xe003),
    "s": String.fromCharCode(0xe004),
    "n": String.fromCharCode(0xe005),
    "m": String.fromCharCode(0xe006),
    "d": String.fromCharCode(0xe007),
    "g": String.fromCharCode(0xe008),
    "p": String.fromCharCode(0xe009),
    "b": String.fromCharCode(0xe00a),
    "h": String.fromCharCode(0xe00b),
    "c": String.fromCharCode(0xe00c),
    "z": String.fromCharCode(0xe00d),
    "l": String.fromCharCode(0xe00e),
    "r": String.fromCharCode(0xe00f),
    "j": String.fromCharCode(0xe010),
    "y": String.fromCharCode(0xe011),
    "w": String.fromCharCode(0xe012),
    "dh": String.fromCharCode(0xe013),
    "kh": String.fromCharCode(0xe014),
    "gh": String.fromCharCode(0xe015),
    "ph": String.fromCharCode(0xe016),
    "bh": String.fromCharCode(0xe017),
    "ṭ": String.fromCharCode(0xe018),
    "ṭ": String.fromCharCode(0xe018), //t + U+0323
    "ḍ": String.fromCharCode(0xe019),
    "ḍ": String.fromCharCode(0xe019), //d + U+0323
    "ṇ": String.fromCharCode(0xe01a),
    "ṇ": String.fromCharCode(0xe01a), //n + U+0323
    "ḷ": String.fromCharCode(0xe01b),
    "ḷ": String.fromCharCode(0xe01b), //l + U+0323
    "ṣ": String.fromCharCode(0xe01d),
    "ṣ": String.fromCharCode(0xe01d), //s + U+0323

    "i": String.fromCharCode(0xe020),
    "u": String.fromCharCode(0xe021),
    "á": String.fromCharCode(0xe022),
    "á": String.fromCharCode(0xe022), //a + U+0301
    "í": String.fromCharCode(0xe023),
    "í": String.fromCharCode(0xe023), //i + U+0301
    "ú": String.fromCharCode(0xe024),
    "ú": String.fromCharCode(0xe024), //u + U+0301
    "e": String.fromCharCode(0xe025),
    "o": String.fromCharCode(0xe026),
    "ai": String.fromCharCode(0xe027),
    "au": String.fromCharCode(0xe028),
    "noV": String.fromCharCode(0xe029),
    "aq": String.fromCharCode(0xe02f),

    ".": String.fromCharCode(0xe02a),
    ",": String.fromCharCode(0xe02b),
    "\"": String.fromCharCode(0xe02c),
    "?": String.fromCharCode(0xe02d),
    "?\"": String.fromCharCode(0xe02e)
}, handler);

var regCons = "(dh|kh|gh|ph|bh|ṭ|ḍ|ṇ|ḷ|ṣ|t|k|x|s|n|m|d|g|p|b|h|c|z|l|r|j|y|w|ṭ|ḍ|ṇ|ḷ|ṣ)";
var regVowel = "(ai|au|á|í|ú|a|i|u|e|o|á|í|ú)";
var regPunc = "(\\?\"| |\"|,|\\.|\\?)";
var reg = new RegExp(`(${regCons}|${regVowel}|${regPunc})`, "g");

var cons = ["dh","kh","gh","ph","bh","ṭ","ḍ","ṇ","ḷ","ṣ","t","k","x","s","n","m","d","g","p","b","h","c","z","l","r","j","y","w","ṭ","ḍ","ṇ","ḷ","ṣ"];
var vowels = ["ai","au","a","i","u","e","o","á","í","ú","á","í","ú"];

function isConsonant(str){
    return (cons.indexOf(str) != -1);
}

function isVowel(str){
    return (vowels.indexOf(str) != -1);
}

function convert(){
    var form = document.getElementById("formSystem");

    switch(form.radioSystem.value){
    case "traditional": convertTraditional(); break;
    case "modern": convertModern(); break;
    }
}

function convertModern(){
    var div = document.getElementById("bhaataan");
    var textarea = document.getElementById("textarea");
    var lines = textarea.value.split(/\r\n|\r|\n/);
    var ch = [];
    var text = "";
    var abbr = document.getElementById("checkAbbr").checked;
    
    div.innerHTML = "";
    
    lines.forEach(function(line,ind,arr){
	if(line == ""){
	    text += "<br>";
	    return;
	}
	
	ch = line.match(reg);

	for(var i=0; i<ch.length; ++i){
	    if(ch[i] == "a"){
		text += map["noC"];

		if(abbr && ch.length-i>2 && isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
		    text += map["aq"];
		    ++i;
		}
		
	    }else if(isVowel(ch[i])){
		text += map["noC"] + map[ch[i]];

		if(abbr && ch.length-i>2 && isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
		    text += map["noV"];
		    ++i;
		}
		
	    }else if(isConsonant(ch[i])){
		if(i<ch.length-1){
		    if(ch[i+1] == "a"){
			text += map[ch[i]];
			++i;

			if(abbr && ch.length-i>2 && isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
			    text += map["noC"] + map["aq"];
			    ++i;
			}
			
		    }else if(isVowel(ch[i+1])){
			text += map[ch[i]] + map["noC"] + map[ch[i+1]];
			++i;

			if(abbr && ch.length-i>2 && isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
			    text += map["noV"];
			    ++i;
			}
			
		    }else{
			text += map[ch[i]] + map["noC"] + map["noV"];
		    }
		}else{
		    text += map[ch[i]] + map["noC"] + map["noV"];
		}
	    }else if(ch[i] == "." || ch[i] == ","){
		text += map[ch[i]];
		if(ch[i+1] == " " && !(ch[i+2] == "\"" || ch[i+2] == "?\"")){
		    ++i;
		}
	    }else{
		text += map[ch[i]];
	    }
	}
	
	text += "<br>";

    });
    
    div.innerHTML = text;
}

function convertTraditional(){
    var div = document.getElementById("bhaataan");
    var textarea = document.getElementById("textarea");
    var lines = textarea.value.split(/\r\n|\r|\n/);
    var ch = [];
    var text = "";
    var abbr = document.getElementById("checkAbbr").checked;
    
    div.innerHTML = "";
    
    lines.forEach(function(line,ind,arr){
	if(line == ""){
	    text += "<br>";
	    return;
	}
	
	ch = line.match(reg);

	for(var i=0; i<ch.length; ++i){
	    if(ch[i] == "a"){
		text += map["noC"];

		if(abbr && ch.length-i>2 && isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
		    text += map["aq"];
		    ++i;
		}
		
	    }else if(isVowel(ch[i])){
		text += map["noC"] + map[ch[i]];

		if(abbr && ch.length-i>2 && isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
		    text += map["noV"];
		    ++i;
		}
		
	    }else if(isConsonant(ch[i])){
		if(i<ch.length-1){
		    if(ch[i+1] == "a"){
			text += map[ch[i]];
			++i;

			if(abbr && ch.length-i>2 && isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
			    text += map["aq"];
			    ++i;
			}
			
		    }else if(isVowel(ch[i+1])){
			text += map[ch[i]] + map[ch[i+1]];
			++i;

			if(abbr && ch.length-i>2 && isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
			    text += map["noV"];
			    ++i;
			}
			
		    }else{
			text += map[ch[i]] + map["noV"];
		    }
		}else{
		    text += map[ch[i]] + map["noV"];
		}
	    }else if(ch[i] == "." || ch[i] == ","){
		text += map[ch[i]];
		if(ch[i+1] == " " && !(ch[i+2] == "\"" || ch[i+2] == "?\"")){
		    ++i;
		}
	    }else{
		text += map[ch[i]];
	    }
	}
	
	text += "<br>";

    });
    
    div.innerHTML = text;
}

function changeFont(){
    var select = document.getElementById("selectFont");
    var option = select.selectedOptions[0];
    var div = document.getElementById("bhaataan");

    div.style.fontFamily = option.value;
}


function changeFont2(){
    var form = document.getElementById("formFont");
    var div = document.getElementById("bhaataan");    
    div.style.fontFamily = form.radioFont.value;
}

window.addEventListener("load", function(){
    changeFont2();
});

