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
		    
		    //newSuggestion.className='suggestion';
		    newSuggestion.setAttribute("class","list-group-item list-group-item-info");
		    console.log("hello");
		    newSuggestion.addEventListener("click",function(){
			replaceInput(id,this.innerHTML);});
		    suggestions.appendChild(newSuggestion);
		    i+=1;
		}
	    }
	});
};

//replaceInput replaces input forms for movies
//This is called when a name is pressed
//This is necessary because simply replacing the value does not update
//the displayed html
var replaceInput = function(id, text){
    var oldInput =document.getElementById(id);
    var name = oldInput.getAttribute("name");
    var type = oldInput.getAttribute("type");
    var newInput= document.createElement("input");
    newInput.setAttribute("type", type);
    newInput.setAttribute("name", name);
    newInput.setAttribute("required","required");
    newInput.setAttribute("class","field");
    newInput.setAttribute("value",text);
    newInput.setAttribute("id",id);
    newInput.addEventListener('keyup', function(){printChar(id);});
    var form = document.getElementById("f1");
    form.replaceChild(newInput,oldInput);
};

//getImages returns a list of the nine image tag names, in a randomly determined order
//the order is determined by backend, and images are set using backend
//Tags: "big", "small", "floor", "bulkhead", "slim", "fan", "window", "central", "ceilingfan"
var getImages = function(e){
    var imageList;
    $.post("/images/",function(d){
	    imageList = JSON.parse(d)['results'];
	    loadImages(imageList);
	});
};
