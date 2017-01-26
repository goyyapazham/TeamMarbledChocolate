var f = document.getElementById("form");
console.log(f);
var create = document.getElementById("create").getAttribute("value");
console.log(create);
if(create=="1"){
    console.log("Creating account");
    f.submit();
}