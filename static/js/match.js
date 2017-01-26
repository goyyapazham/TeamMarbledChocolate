var home = function(d){
    var f = document.createElement("form");
    f.setAttribute("action","/home/");
    f.submit();
};
var logout = function(d){
    var f = document.createElement("form");
    f.setAttribute("action","/logout/");
    f.setAttribute("method","POST");
    f.submit();
};

var startChat = function(user, recip){
    console.log(user);
    console.log(recip);
    var f = document.createElement("form");
    f.setAttribute("action","/startChat/");
    f.setAttribute("method","POST");
    var username = document.createElement("input");
    username.setAttribute("name","user");
    username.setAttribute("value",user);
    f.appendChild(username);
    username = document.createElement("input");
    username.setAttribute("name","recip");
    username.setAttribute("value",recip);
    f.appendChild(username);
    f.submit();
};

var assignMatchButtons = function(e){
    var buttons = document.getElementsByTagName("button");
    console.log(buttons);
    var button;
    for(var i = 0; i<buttons.length; i++){
        button = buttons[i];
        if(button.getAttribute("id")=="startbutton"){
            button.addEventListener("click",function(){startChat(this.getAttribute("name"),this.getAttribute("value"));});
        }
    }
};


document.getElementById("homebutton").addEventListener("click",home);                                                                                                                                   
document.getElementById("logoutbutton").addEventListener("click",logout);
assignMatchButtons();



