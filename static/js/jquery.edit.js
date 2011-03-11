$(document).ready(function() {
    $('#editable').blur(function() {
        var newValue = $(this).text();
        // do something         
        // For example, you could place an AJAX call here:  
        $.ajax({
           type: "POST",
           url: window.location.pathname,
           data: "text=" + newValue,
           success: function(msg){
             alert( "Data Saved: " + msg );
           }
        });
    });
});
