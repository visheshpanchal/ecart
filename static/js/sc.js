


  // Get today's date and time


function startTimer(duration) {
    var timer = duration;
    
    var x = setInterval(function () {
        hour  = parseInt (timer / 3600 ,10);
        minutes = parseInt((timer % 3600) / 60 , 10);
        seconds = parseInt(timer % 60, 10);

        
        hour = hour < 10 ? "0" + hour : hour;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        document.querySelector("#timer_hours").textContent = hour;
        document.querySelector("#timer_min").textContent =  minutes ;
        document.querySelector("#timer_sec").textContent =  seconds;



        if (--timer < 0) {
           clearInterval(x);
        }
    }, 1000);
}



try{
    var is_bool = Boolean($("#timer_value").attr("value"));

}
catch (e){
    var is_bool = false;
}

if (is_bool)
{
    window.onload = function () {
        var fiveMinutes = $("#timer_hidden_value").attr("value");
        
        startTimer(fiveMinutes);
    };
    
}