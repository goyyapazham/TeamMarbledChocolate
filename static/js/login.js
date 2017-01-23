//The login page is a single html page which cycles through inputs

//State checks which of the "pages" are being displayed
var state = "login";
//form and button elements are the core of all functions
var form = document.getElementById("f1");
var button = document.getElementById("b1");

//makeHidden hides all of the forms. This is used when reloading the "page"
//All loadRegister functions hide previous responses, and add to the form
var makeHidden = function(e){
    var inputs = document.getElementsByTagName("input");
    for(var i =0; i<inputs.length;i++){
	inputs[i].setAttribute("type","hidden");
    }
    return 0;
};

//killImages deletes all the images. Neccesary because image files use a slightly
// different way of submitting
//This makes a generic input tag
var killImages = function(e){
    var images = document.getElementsByTagName("img");
    while(images.length>0){
	images[0].remove();
    }
    return 0;
}

var makeInput = function(type, name, text){
    var ret = document.createElement("input");
    ret.setAttribute("type", type);
    ret.setAttribute("name", name);
    ret.setAttribute("required","required");
    ret.setAttribute("class","field");
    ret.setAttribute("value",text);
    return ret;
};

var makeInputImage = function(name){
    var ret = document.createElement("input");
    ret.setAttribute("type", "file");
    ret.setAttribute("name", name);
    ret.setAttribute("class","field");
    ret.setAttribute("accept","image/*");
    ret.setAttribute("id","pfp");
    return ret;
};

//setDescription sets the value in the description heading
var setDescription = function(text){
    document.getElementById("description").innerHTML=text;
};

//loadRegister1 loads inputs for username, email, password, and repeat password
var loadRegister1 = function(e){
    makeHidden();
    setDescription("Enter your username, email address, password, and reenter your password");
    form.appendChild(makeInput("text","user","Username"));
    form.appendChild(makeInput("text","email","Email"));
    form.appendChild(makeInput("password","p1","Password"));
    form.appendChild(makeInput("password","p2","Password"));
};

//loadRegister2 loads input for gender you are, gender you want to data,
//and security question
var loadRegister2 = function(e){
    makeHidden();
    setDescription("Enter your gender identity, and the gender(s) you're interested in being matched with. Next answer the security question for retrieving you password: Who do you secretly have a crush on?");
    //YO IF U DO FRONTEND CHECK THIS OUT
    //HI ELY
    //CAN U MAKE THIS A DROPDOWN (i.e., male, female, other: please specify) so that matching users up is easier?
    //OK I'LL TRY
    form.appendChild(makeInput("text","gender","Your gender"));
    form.appendChild(makeInput("text","pref","Gender(s) you're looking for"));
    form.appendChild(makeInput("text","security","Ely Sandine"));
};

//loadRegister3 loads input for your favorite movie, and adds autocomplete
var loadRegister3 = function(e){
    makeHidden();
    setDescription("Enter your three favorite movies. Suggestions will appear below as you type");
    var m;
    for(var i = 0; i<3; i++){
	m = makeInput("text","m"+i,"Movie"+i);
	m.addEventListener('keyup', function(){printChar(this.getAttribute("name"));});
	form.appendChild(m);
	m = makeInput("hidden","movie"+i, "NONE");
	m.setAttribute("id","m"+i);
	form.appendChild(m);
    }
    var suggestions = document.createElement("div");
    suggestions.setAttribute("id","suggestions");
    form.appendChild(suggestions);
};

//loadRegister4 loads images of air conditioners for you to choose
var loadRegister4 = function(e){
    makeHidden();
    var suggestions = document.getElementsByTagName("div")[0];
    suggestions.remove();
    var hinput;//Hidden input fields store image preferences
    for(var i = 0; i<3; i++){
	hinput=makeInput("hidden","i"+i, "NONE");
	hinput.setAttribute("id","i"+i);
	form.appendChild(hinput);
    }
    getImages();
};

//loadImages takes a list of image tags and then adds the images to the form with eventlisteners
var loadImages = function(d){
    var image;
    for(var i = 0; i<d.length; i++){
	image = document.createElement("img");
	image.setAttribute("src","../../static/images/img"+i+".jpg");
	image.setAttribute("alt",d[i]);
	image.addEventListener("click", function(e){updateAC(this.getAttribute("alt"),0);});
	form.appendChild(image);
    }
};

//updateAC takes a tag name then adds it to one of the preferences
var updateAC = function(tag, index){
    if(index<3){
	var input = document.getElementById("i"+index);
	if(input.getAttribute("value")=="NONE"){
	    input.setAttribute("value",tag);
	}else{
	    updateAC(tag, index+1);//WOOHOO RECURSION
	}
    }
};

//reset form resets the entire form
var resetForm = function(e){
    var inputs = document.getElementsByTagName("input");
    while(inputs.length>0){
	inputs[0].remove();
    }
}

//loadRegister5 loads inputs for image, bio
var loadRegister5 = function(e){
    killImages();
    makeHidden();
    setDescription("Lastly, enter your bio, and then upload a profile picture");
    form.appendChild(makeInput("text","bio","Bio"));
    form.appendChild(makeInputImage("pfp"));
};



var loginButton = function(e){
    resetForm();
    killImages();
    var button = document.getElementById("b1");
    form.appendChild(makeInput("text","user","Username"));
    form.appendChild(makeInput("password","password","Password"));
    button.setAttribute("type","submit");
    form.setAttribute("action","/authenticate/");
    state="login"
};

var regButton = function(e){
    resetForm();
    button.setAttribute("type","button");
    form.setAttribute("action","/create/");
    state="reg1"
    loadRegister1();
};

//next triggers when the button at the bottom is clicked
//it checks the state, and calls the function
var next = function(e){
    if(state=="reg1"){
	state = "reg2";
	loadRegister2();
    }else if(state=="reg2"){
	state = "reg3";
	loadRegister3();
    }else if(state=="reg3"){
	state="reg4"
	loadRegister4();
    }else if(state=="reg4"){
	state="reg5"
	loadRegister5();
    }else if(state=="reg5" || state=="login"){
	form.submit();
    }
};

//TRIGGERS
button.addEventListener("click", next);
document.getElementById("loginbutton").addEventListener("click",loginButton);
document.getElementById("registerbutton").addEventListener("click",regButton);
