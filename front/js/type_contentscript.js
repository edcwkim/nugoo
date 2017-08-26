alert('hi');
var word = "hello";
var input = "";
document.body.addEventListener('keypress',function(ev){
    input += String.fromCharCode(ev.keyCode);
    console.log(input);
    if(input == word){
        alert('typed hello');
        input = "";
    }
});

// reset input when pressing esc
document.body.addEventListener('keyup',function(ev){
    if(ev.keyCode == 27) input = "";
});