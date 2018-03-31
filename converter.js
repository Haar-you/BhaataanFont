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
    "ḍ": String.fromCharCode(0xe019),
    "ṇ": String.fromCharCode(0xe01a),
    "ḷ": String.fromCharCode(0xe01b),
    "ṣ": String.fromCharCode(0xe01d),

    "i": String.fromCharCode(0xe020),
    "u": String.fromCharCode(0xe021),
    "á": String.fromCharCode(0xe022),
    "í": String.fromCharCode(0xe023),
    "ú": String.fromCharCode(0xe024),
    "e": String.fromCharCode(0xe025),
    "o": String.fromCharCode(0xe026),
    "ai": String.fromCharCode(0xe027),
    "au": String.fromCharCode(0xe028),
    "noV": String.fromCharCode(0xe029),

    ".": String.fromCharCode(0xe02a),
    ",": String.fromCharCode(0xe02b),
    "\"": String.fromCharCode(0xe02c),
    "?": String.fromCharCode(0xe02d),
    "?\"": String.fromCharCode(0xe02e)
}, handler);

var regCons = "(dh|kh|gh|ph|bh|t|k|x|s|n|m|d|g|p|b|h|c|s|l|r|j|y|w|ṭ|ḍ|ṇ|ḷ|ṣ|z)";
var regVowel = "(ai|au|a|i|u|e|o|á|í|ú)";
var regPunc = "(\\?\"| |\"|,|\.|\\?)";
var reg = new RegExp("("+regCons+"|"+regVowel+"|"+regPunc+")", "g");

var cons = ["dh","kh","gh","ph","bh","t","k","x","s","n","m","d","g","p","b","h","c","s","l","r","j","y","w","ṭ","ḍ","ṇ","ḷ","ṣ","z"];
var vowels = ["ai","au","a","i","u","e","o","á","í","ú"];

function isConsonant(str){
    return (cons.indexOf(str) != -1);
}

function isVowel(str){
    return (vowels.indexOf(str) != -1);
}


function convert(){
    var div = document.getElementById("bhaataan");
    var textarea = document.getElementById("textarea");
    var lines = textarea.value.split(/\r\n|\r|\n/);
    var ch = [];
    var text = "";

    div.innerHTML = "";
    
    lines.forEach(function(line,ind,arr){
	ch = line.match(reg);


	for(var i=0; i<ch.length; ++i){
	    if(ch[i] == "a"){
		text += map["noC"];
	    }else if(isVowel(ch[i])){
		if(i>=1 && isConsonant(ch[i-1])){
		    text += map[ch[i]];
		}else{
		    text += map["noC"] + map[ch[i]];
		}
	    }else if(isConsonant(ch[i])){
		if(i<ch.length-1){
		    if(ch[i+1] == "a"){
			text += map[ch[i]];
			i+=1;
		    }else if(isVowel(ch[i+1])){
			text += map[ch[i]];
		    }else{
			text += map[ch[i]] + map["noV"];
		    }
		}else{
		    text += map[ch[i]] + map["noV"];
		}
	    }else{
		text += map[ch[i]];
	    }
	}
	
	text += "<br>";

    })
    div.innerHTML = text;
}
