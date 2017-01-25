var logout = function(d){
    var f = document.createElement("form");
    f.setAttribute("action","/logout/");
    f.setAttribute("method","POST");
    f.submit();
}

document.getElementById("logoutbutton").addEventListener("click",logout);
