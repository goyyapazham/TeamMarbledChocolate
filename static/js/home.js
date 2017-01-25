var logout = function(d){
    var f = document.createElement("form");
    f.setAttribute("action","/logout/");
    f.setAttribute("method","POST");
    f.submit();
};

var match = function(user){
    var f = document.createElement("form");
    f.setAttribute("action","/match/");
    f.setAttribute("method","POST");
    var username = document.createElement("input");
    username.setAttribute("name","user");
    username.setAttribute("value",user);
    f.appendChild(username);
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
}

document.getElementById("logoutbutton").addEventListener("click",logout);
document.getElementById("matchbutton").addEventListener("click",function(){match(this.getAttribute("value"));});
document.getElementById("startbutton").addEventListener("click",function(){startChat(this.getAttribute("name"),this.getAttribute("value"));});
