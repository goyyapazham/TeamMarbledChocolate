var logout = function(d){
    var f = document.createElement("form");
    f.setAttribute("action","/logout/");
    f.setAttribute("method","POST");
    f.submit();
}

var match = function(user){
    var f = document.createElement("form");
    f.setAttribute("action","/match/");
    f.setAttribute("method","POST");
    var username = document.createElement("input");
    username.setAttribute("name","user");
    username.setAttribute("value",user);
    f.appendChild(username);
    f.submit();
}

document.getElementById("logoutbutton").addEventListener("click",logout);
document.getElementById("matchbutton").addEventListener("click",function(){match(this.getAttribute("value"));});
