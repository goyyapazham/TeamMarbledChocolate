//This function triggers when a user types, and creates suggestions
var printChar = function(e){
    var start = document.getElementById("field").value;
    var input = {'text' : start}
    $.ajax({
	    url: '/process/',//Backend function returns list of suggestions
		type: 'POST',
		data: input,
		success: function (d){
		d=JSON.parse(d);
		var suggestions = document.getElementById("suggestions");
		console.log(suggestions.length);
		var i=0;
		var currentSuggestion;
		var oldsuggestions = document.getElementsByClassName("suggestion");
		//Deletes old suggestions
		while(oldsuggestions.length>0){
		    currentSuggestion=oldsuggestions[0];
		    currentSuggestion.remove();
		}
		//Creates new suggestions
		while(i < d['results'].length){
		    newSuggestion=document.createElement("li");
		    newSuggestion.innerHTML=d['results'][i];
		    newSuggestion.className='suggestion';
		    suggestions.appendChild(newSuggestion);
		    i+=1;
		}
	    }
	});
};

var trigger = document.getElementById('field');
trigger.addEventListener('keyup', printChar);
