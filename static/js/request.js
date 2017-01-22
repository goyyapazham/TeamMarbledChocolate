//This function triggers when a user types, and creates suggestions
var printChar = function(id){
    var start = findId(id).value;
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
		var oldsuggestions = document.getElementsByTagName("li");
		//Deletes old suggestions
		while(oldsuggestions.length>0){
		    currentSuggestion=oldsuggestions[0];
		    currentSuggestion.remove();
		}
		//Creates new suggestions
		var keys = Object.keys(d['results']);
		while(i < keys.length){
		    newSuggestion=document.createElement("li");
		    newSuggestion.innerHTML=d['results'][keys[i]];
		    newSuggestion.className='suggestion';
		    newSuggestion.setAttribute("class","list-group-item list-group-item-info");
		    //id stores the id of the movie
		    newSuggestion.setAttribute("id", keys[i]);
		    newSuggestion.addEventListener("click",function(){
			    replaceInput(id, this.innerHTML, this.getAttribute("id"))});
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
//The val is also replaced in the hidden form
var replaceInput = function(id, text, val){
    var oldInput =findId(id);
    var name = oldInput.getAttribute("name");
    var type = oldInput.getAttribute("type");
    var newInput= document.createElement("input");
    newInput.setAttribute("type", type);
    newInput.setAttribute("name", name);
    newInput.setAttribute("required","required");
    newInput.setAttribute("class","field");
    newInput.setAttribute("value",text);
    newInput.addEventListener('keyup', function(){printChar(id);});
    var form = document.getElementById("f1");
    form.replaceChild(newInput,oldInput);
    form = document.getElementById(id);
    form.setAttribute("value", val);
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

//findId(id) is used as a fake getElementByName for forms. This deals with the 
// tricky situation with suggestions
var findId = function(id){
    var inputs = document.getElementsByTagName("input");
    for(var i = 0; i< inputs.length;i++){
	if(inputs[i].getAttribute('name')==id){
	    return inputs[i];
	}
    }
    return "NONE";
};
