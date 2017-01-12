//THis function triggers when a user types, and creates suggestions
var printChar = function(e){
    var start = document.getElementById("field").value;
    var input = {'text' : start}
    console.log(input);
    $.ajax({
	    url: '/process/',
		type: 'POST',
		data: input,
		success: function (d){
		console.log(d);
	    }
	});
};

console.log("hello ely");
var trigger = document.getElementById('field');
console.log(trigger);
trigger.addEventListener('keyup', printChar);
