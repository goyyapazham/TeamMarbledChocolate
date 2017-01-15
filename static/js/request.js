//This function triggers when a user types, and creates suggestions
var printChar = function(id){
    var start = document.getElementById(id).value;
    var input = {'text' : start}
    $.ajax({
	    url: '/suggest/',//Backend function returns list of suggestions
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
			    var oldInput =document.getElementById(id);
			    var name = oldInput.getAttribute("name");
			    var type = oldInput.getAttribute("type");
			    var newInput= document.createElement("input");
			    newInput.setAttribute("type", type);
			    newInput.setAttribute("name", name);
			    newInput.setAttribute("required","required");
			    newInput.setAttribute("class","field");
			    newInput.setAttribute("value",this.innerHTML);
			    newInput.setAttribute("id",id);
			    newInput.addEventListener('keyup', function(){printChar(id);});
			    var form = document.getElementById("f1");
			    form.replaceChild(newInput,oldInput);
			    return input;});
		    suggestions.appendChild(newSuggestion);
		    i+=1;
		}
	    }
	});
};
