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

document.getElementById("homebutton").addEventListener("click",home);      
document.getElementById("logoutbutton").addEventListener("click",logout);

