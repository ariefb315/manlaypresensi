$(document).ready(function() {
    var counter = 0;
    $("#btn-notif").on("click", function(){
        counter++;
        console.log($("span.badge-light").text(), counter);
        $("span.badge-light").text(counter);

    });
});