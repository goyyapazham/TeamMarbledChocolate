//THis function triggers when a user types, and creates suggestions
var printChar = function(e){
    var start = document.getElementById("field").value;
    var input = {'text' : start}
    console.log(input);
    $.ajax({
	    url: '/process/',
		type: 'POST',
		data: input,
		success: function (d){
		d=JSON.parse(d);
		console.log(d['results']);
		var i = 0;
		var suggestion = document.getElementById("suggestions");
		var newSuggestion;
		while(i < d['results'].length){
		    newSuggestion=document.createElement("li");
		    newSuggestion.innerHTML=d['results'][i];
		    suggestions.appendChild(newSuggestion);
		    i+=1;
		}
	    }
	});
};

console.log("hello ely");
var trigger = document.getElementById('field');
console.log(trigger);
trigger.addEventListener('keyup', printChar);
