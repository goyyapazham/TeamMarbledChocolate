var printChar = function(char){
    console.log(char);
}
var trigger = document.getElementByTagName("form");
var keyboard = KeyboardEvent();
trigger.addEventListener('keyup', (keyboard.char));
