//The login page is a single html page which cycles through inputs

//State checks which of the "pages" are being displayed
var state = "login";

//makeHidden hides all of the forms. This is used when reloading the "page"
//All loadRegister functions hide previous responses, and add to the form
var makeHidden = function(e){
    var inputs = document.getElementsByTagName("input");
    for(var i =0; i<inputs.length;i++){
	inputs[i].setAttribute("type","hidden");
    }
    return 0;
};

//This makes a generic input tag
var makeInput = function(type, name, text){
    var ret = document.createElement("input");
    ret.setAttribute("type", type);
    ret.setAttribute("name", name);
    ret.setAttribute("required","required");
    ret.setAttribute("class","field");
    ret.setAttribute("value",text);
    return ret;
};

//setDescription sets the value in the description heading
var setDescription = function(text){
    document.getElementById("description").innerHTML=text;
};

//loadRegister1 loads inputs for username, email, password, and repeat password
var loadRegister1 = function(e){
    makeHidden();
    var form = document.getElementById("f1");
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
    var form = document.getElementById("f1");
    setDescription("Enter your sexuality, and the sexuality of person you would like to date. Next answer the security question for retrieving you password: Who do you secretly have a crush on?");
    form.appendChild(makeInput("text","you","Your sexuality"));
    form.appendChild(makeInput("text","preference","Sexuality you want to date"));
    form.appendChild(makeInput("text","security","Ely Sandine"));
};

//loadRegister3 loads input for your favorite movie, and adds autocomplete
var loadRegister3 = function(e){
    makeHidden();
    var form = document.getElementById("f1");
    setDescription("Enter your three favorite movies. Suggestions will appear below as you type");
    var m;
    for(var i = 0; i<3; i++){
	m = makeInput("text","m"+i,"Movie"+i);
	m.setAttribute("id","m"+i);
	m.addEventListener('keyup', function(){printChar(this.getAttribute("id"));});
	form.appendChild(m);
    }
    var suggestions = document.createElement("ol");
    suggestions.setAttribute("id","suggestions");
    form.appendChild(suggestions);
}
//next triggers when the button at the bottom is clicked
//it checks the state, and calls the function
var next = function(e){
    if(state=="login"){
	state = "reg1";
	loadRegister1();
    }else if(state=="reg1"){
	state = "reg2";
	loadRegister2();
    }else if(state=="reg2"){
	state = "reg3";
	loadRegister3();
    }
};

//TRIGGERS
var button = document.getElementById("b1");
button.addEventListener("click", next);