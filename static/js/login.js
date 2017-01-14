var makeHidden = function(e){
    var form = document.getElementsByTagName("input");
    for(var i =0; i<form.length;i++){
	form[i].type="hidden";
    }
    
}

var button = document.getElementById("b1");
button.addEventListener("click", makeHidden);