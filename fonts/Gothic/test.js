window.addEventListener("load", function(){
    var div = document.getElementById("bhaataan");
    var text = "";

    text += `<div>${range(0xe000, 0xe01d).map(c => String.fromCharCode(c)).join("")}</div>`;

    text += range(0xe020, 0xe029).map(v =>
				      `<div>${range(0xe000, 0xe01d).map(c => String.fromCharCode(c, v)).join("")}</div>`
				     ).join("");

    text += range(0xe020, 0xe028).map(v =>
				      `<div>${range(0xe000, 0xe01d).map(c => String.fromCharCode(c, v, 0xe029)).join("")}</div>`
				     ).join("");
    
    text += `<div>${range(0xe000, 0xe01d).map(x => String.fromCharCode(x, 0xe02f)).join("")}</div>`;
    
    text += `<div>${range(0xe020, 0xe029).concat([0xe02f]).map(x => String.fromCharCode(x)).join("")}</div>`;

    text += range(0xe000, 0xe01d).map(c => 
				      `<div>${
(range(0xe020, 0xe029).concat([0xe02f])).map(v => String.fromCharCode(c, v)).concat(
range(0xe020, 0xe028).map(v => String.fromCharCode(c, v, 0xe029))
).join("")
}</div>`
				     ).join("");
    
    text += `<div>${range(0xe02a, 0xe02e).map(x => String.fromCharCode(x)).join("")}</div>`;

    div.innerHTML = text;

});

function range(a, b){
    var arr = [];
    for(var i=a; i<=b; ++i){
	arr.push(i);
    }
    return arr;
}


