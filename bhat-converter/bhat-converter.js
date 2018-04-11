var Bhat = function(){};

Bhat.map = new Proxy({
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
}, {
    get : function(target, name){
	return name in target ? target[name] : name;
    }
});

Bhat.regConsonant = "(dh|kh|gh|ph|bh|ṭ|ḍ|ṇ|ḷ|ṣ|t|k|x|s|n|m|d|g|p|b|h|c|z|l|r|j|y|w|ṭ|ḍ|ṇ|ḷ|ṣ)";
Bhat.regVowel = "(ai|au|á|í|ú|a|i|u|e|o|á|í|ú)";
Bhat.regPunc = "(\\?\"| |\"|,|\\.|\\?|.)";
Bhat.reg = new RegExp(`(${Bhat.regConsonant}|${Bhat.regVowel}|${Bhat.regPunc})`, "g");

Bhat.consonants = ["dh","kh","gh","ph","bh","ṭ","ḍ","ṇ","ḷ","ṣ","t","k","x","s","n","m","d","g","p","b","h","c","z","l","r","j","y","w","ṭ","ḍ","ṇ","ḷ","ṣ"];
Bhat.vowels = ["ai","au","a","i","u","e","o","á","í","ú","á","í","ú"];

Bhat.isConsonant = function(str){
    return (Bhat.consonants.indexOf(str) != -1);
};

Bhat.isVowel = function(str){
    return (Bhat.vowels.indexOf(str) != -1);
};



Bhat.convert = function(input, abbr, mode){
    var ch = [];
    var text = [];
    
    ch = input.match(Bhat.reg);

    if(ch == null) return "";

    for(var i=0; i<ch.length; ++i){
	if(ch[i] == "a"){
	    text.push(Bhat.map["noC"]);

	    if(abbr && Bhat.isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
		text.push(Bhat.map["aq"]);
		++i;
	    }
	}else if(Bhat.isVowel(ch[i])){
	    text.push(Bhat.map["noC"]);
	    text.push(Bhat.map[ch[i]]);

	    if(abbr && Bhat.isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
		text.push(Bhat.map["noV"]);
		++i;
	    }
	}else if(Bhat.isConsonant(ch[i])){
	    if(ch[i+1] == "a"){
		text.push(Bhat.map[ch[i]]);
		++i;

		if(abbr && Bhat.isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
		    text.push(mode ? Bhat.map["noC"] : "");
		    text.push(Bhat.map["aq"]);
		    ++i;
		}
	    }else if(Bhat.isVowel(ch[i+1])){
		text.push(Bhat.map[ch[i]]);
		text.push((mode ? Bhat.map["noC"] : ""));
		text.push(Bhat.map[ch[i+1]]);
		++i;

		if(abbr && Bhat.isConsonant(ch[i+1]) && ch[i+1] == ch[i+2]){
		    text.push( Bhat.map["noV"]);
		    ++i;
		}
	    }else{
		text.push(Bhat.map[ch[i]]);
		text.push((mode ? Bhat.map["noC"] : ""));
		text.push(Bhat.map["noV"]);
	    }
	}else if(ch[i] == "." || ch[i] == ","){
	    text.push( Bhat.map[ch[i]]);
	    if(ch[i+1] == " " && !(ch[i+2] == "\"" || ch[i+2] == "?\"")){
		++i;
	    }
	}else{
	    text.push(Bhat.map[ch[i]]);
	}
    }
    
    return text.join("");
};
