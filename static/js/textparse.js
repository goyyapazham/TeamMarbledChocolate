var printChar = function(e){
    var input = document.getElementById("field").value;
    console.log(input);
};

console.log("hello ely");
var trigger = document.getElementById('field');
console.log(trigger);
trigger.addEventListener('keyup', printChar);
