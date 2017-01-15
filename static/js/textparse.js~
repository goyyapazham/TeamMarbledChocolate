//This function triggers when a user types, and creates suggestions
var printChar = function(id){
    var start = document.getElementById(id).value;
    var input = {'text' : start}
    $.ajax({
	    url: '/process/',//Backend function returns list of suggestions
	    type: 'POST',
	    data: input,
	    success: function (d){
		d=JSON.parse(d);
		var suggestions = document.getElementById("suggestions");
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
		    newSuggestion.addEventListener("click",function(){
			    var input =document.getElementById(id);
			    input.setAttribute("value",this.innerHTML);
			    input.setAttribute("type","hidden");});
		    suggestions.appendChild(newSuggestion);
		    i+=1;
		}
	    }
	});
};
